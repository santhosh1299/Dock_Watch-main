import urllib.request
import json
import pandas as pd
import datetime, pytz
import schedule
import time

# Urls
url_gbfs= "https://gbfs.bcycle.com/bcycle_boulder/gbfs.json"
url_gbfs_versions= "https://gbfs.bcycle.com/bcycle_boulder/gbfs_versions.json"
url_system_information= "https://gbfs.bcycle.com/bcycle_boulder/system_information.json"
url_station_information= "https://gbfs.bcycle.com/bcycle_boulder/station_information.json"
url_station_status= "https://gbfs.bcycle.com/bcycle_boulder/station_status.json"
url_system_pricing_plans= "https://gbfs.bcycle.com/bcycle_boulder/system_pricing_plans.json"
url_system_regions= "https://gbfs.bcycle.com/bcycle_boulder/system_regions.json"


def data_collection():
    # Reading station information document and extracting the required data
    with urllib.request.urlopen(url_station_information) as url:
        data_station = json.load(url)
        #print(data_station)

    df_stations=pd.DataFrame(i for i in data_station['data']['stations'])
    df_stations['last_updated']= data_station['last_updated']
    df_stations.drop(columns= ['rental_uris'],inplace=True)
    #df_stations.head()

    # Reading station status information document and extracting the required data
    with urllib.request.urlopen(url_station_status) as url:
        data_status = json.load(url)
        #print(data_status)

    df_status=pd.DataFrame(i for i in data_status['data']['stations'])
    df_status['electic_bikes_available']= [i['num_bikes_available_types']['electric'] for i in data_status['data']['stations']]
    df_status['smart_bikes_available']= [i['num_bikes_available_types']['smart'] for i in data_status['data']['stations']]
    df_status['classic_bikes_available']= [i['num_bikes_available_types']['classic'] for i in data_status['data']['stations']]
    df_status.drop(columns='num_bikes_available_types',inplace= True)
    #df_status.head()

    # Merging the stations and status data 
    df_merged= pd.merge(df_stations,df_status,on='station_id',how='outer')

    # Reordering and renaming the columns
    column_order = ["last_updated", "last_reported", "station_id", "name", "address", "lon", "lat", "is_returning", "is_renting", "is_installed", "_bcycle_station_type", "num_docks_available", "num_bikes_available", "electic_bikes_available", "smart_bikes_available", "classic_bikes_available"]
    column_rename= {"last_updated": "station_last_updated", "last_reported": "status_last_reported", "name":"station_name","address":"station_address","lon":"station_longitude","lat": "station_latitude","is_returning":"station_is_returning","is_renting":"station_is_renting","is_installed":"station_is_installed","_bcycle_station_type":"station_type","num_docks_available":"docks_available","num_bikes_available":"bikes_available"}
    df_merged= df_merged[column_order]
    df_merged.rename(columns = column_rename, inplace = True)
    time_of_collection= datetime.datetime.now(pytz.timezone('US/Mountain')).strftime('%m-%d-%y %H:%M:%S')
    df_merged['datatime_mtd']= time_of_collection
    #df_merged.head()

    # Concatenate the new data to the existing data
    df_existing= pd.read_csv(r"C:\Data Mining BCycle Data Collection\Bcycle_data_to_date.csv")
    df_final= pd.concat([df_existing,df_merged])

    df_final.to_csv(r"C:\Data Mining BCycle Data Collection\Bcycle_data_to_date.csv", index=False)

    print("Completed Data Time: ",time_of_collection)

    # Recording logs 
    log= pd.read_csv(r"C:\Data Mining BCycle Data Collection\Automation_logs.csv")
    new_log = pd.Series([df_merged['datatime_mtd'][0], df_merged.shape[0],df_final.shape[0]], index=log.columns)
    log = log._append(new_log,ignore_index=True)
    log.to_csv(r"C:\Data Mining BCycle Data Collection\Automation_logs.csv", index=False)

schedule.every(1).minutes.do(data_collection)

while 1:
    schedule.run_pending()
    time.sleep(1)
