# Boulder BCycle Wait-time Estimation
<div class='tableauPlaceholder' id='viz1711327857533' style='position: relative'>
  <noscript>
    <a href='#'>
      <img alt='Dashboard 1' src='https://public.tableau.com/static/images/Bo/BoulderBcycleWaitTimeEstimation/Dashboard1/1_rss.png' style='border: none' />
    </a>
  </noscript>
  <object class='tableauViz' style='display:none;'>
    <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
    <param name='embed_code_version' value='3' />
    <param name='site_root' value='' />
    <param name='name' value='BoulderBcycleWaitTimeEstimation&#47;Dashboard1' />
    <param name='tabs' value='no' />
    <param name='toolbar' value='yes' />
    <param name='static_image' value='https://public.tableau.com/static/images/Bo/BoulderBcycleWaitTimeEstimation/Dashboard1/1.png' />
    <param name='animate_transition' value='yes' />
    <param name='display_static_image' value='yes' />
    <param name='display_spinner' value='yes' />
    <param name='display_overlay' value='yes' />
    <param name='display_count' value='yes' />
    <param name='language' value='en-US' />
    <param name='filter' value='publish=yes' />
  </object>
</div>

<script type='text/javascript'>
  var divElement = document.getElementById('viz1711327857533');
  var vizElement = divElement.getElementsByTagName('object')[0];
  if (divElement.offsetWidth > 800) {
    vizElement.style.width='100%';
    vizElement.style.height=(divElement.offsetWidth*0.75)+'px';
  } else if (divElement.offsetWidth > 500) {
    vizElement.style.width='100%';
    vizElement.style.height=(divElement.offsetWidth*0.75)+'px';
  } else {
    vizElement.style.width='100%';
    vizElement.style.height='877px';
  }
  var scriptElement = document.createElement('script');
  scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
  vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>


[Presentation Link](https://www.youtube.com/watch?v=QEBMTk4OsAE)    

**About:**
Boulder BCycle is a popular and convenient transportation service in Boulder, Colorado. It offers electric bikes stationed throughout the city, providing a sustainable and efficient means of commuting. Notably, the service is tailored to the needs of the community, as it offers a unique benefit to students by providing them with free rides for up to one hour per trip. This student-friendly policy makes it an attractive choice for the University of Colorado Boulder's student population, who frequently utilize Boulder BCycle to commute between their residences and the university. The service plays a key role in the city's transport system, supporting sustainability goals and meeting student needs.

In Boulder's BCycle system, users often encounter reliability issues and struggle to predict bike station availability. This project, as part of the **CSCI 5502- Data Mining** course, **focuses on transforming the BCycle experience by dissecting usage patterns and calculating waiting times for each station**. By analyzing historical data and real-time inputs, we aim to provide users with valuable insights, enabling them to make informed decisions about when and where to pick up a bike. This initiative seeks to enhance the overall convenience and efficiency of the service, ultimately making BCycle an even more reliable and accessible mode of transportation for the Boulder community.

  

**Challenges:**
* **Data Availability**: Historical BCycle station status data is currently unavailable, as only real-time data is accessible. Consequently, we've been consistently collecting data in the background for our analysis.
* **Data Inconsistency**: The data is gathered continuously in the background using an AWS EC2 instance, but it occasionally experiences interruptions, causing breaks in the data. External factors such as Colorado's Daylight Saving Time also introduce additional complexity.
* **Data Sampling Limitations**: Numerous variables, such as public transport availability, weather conditions, and class schedules, influence BCycle usage. It's important to acknowledge that our data sample may not encompass all these influencing factors

**Approach Overview:**
1. **Data Collection & Storage**: Collect live data from GBFS (General Bikeshare Feed Specification) and store it in an SQL server to maintain historical records.
2. **Data Preprocessing Pipeline**: Develop a data preprocessing pipeline to calculate additional features and ensure data quality.
3. **Exploratory Data Analysis**: Conduct Exploratory Data Analysis (EDA) using a dashboard to identify and understand usage patterns within the dataset.
4. **Forecasting Model Development**: Build a predictive model to forecast waiting times for each station, utilizing the pre-processed data.

**Data Flow Architecture**

![image](https://github.com/Niranjan-Cholendiran/Dock_Watch/assets/78549555/918cd3c9-5492-49f0-9b64-d1bce56b77f7)


