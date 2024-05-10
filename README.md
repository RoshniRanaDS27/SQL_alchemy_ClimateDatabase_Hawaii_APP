# Holiday vacation in Honolulu, Hawaii
# Climate Database 

In this section, 
Have used Python and SQLAlchemy to do a basic climate analysis and data exploration of climate database. 
Specifically, have used SQLAlchemy ORM queries, Pandas, and Matplotlib.

After completting the initial analysis, 
have designed a Flask API based on the queries that was just developed. 
To do so, used the Flask to create routes. 

# Background
A long holiday vacation in Honolulu, Hawaii. 
To help with trip planning, have decided to do a climate analysis about the area. 
The following sections outline the steps that are considered to take to accomplish this task.
Task was broken down into the following tasks:

Part 1: Analyze and Explore the Climate Data
Part 2: Designning Climate App

# Part 1: Analyze and Explore the Climate Data
In this section, have used Python and SQLAlchemy to do a basic climate analysis and data exploration of climate database. 
Specifically, used SQLAlchemy ORM queries, Pandas, and Matplotlib.     
To do so, complete the following steps:


Used the SQLAlchemy "create_engine()" function to connect to SQLite database.
Used the SQLAlchemy "automap_base()" function to reflect tables into classes, and then saved references to the classes named station and measurement.

Linked Python to the database by creating a SQLAlchemy session.
closed session at the end of the notebook.

# Performed a precipitation analysis and then a station analysis by completing the steps in the following two subsections.

# Precipitation Analysis
1. Found the most recent date in the dataset.
2. By Using that date, got the previous 12 months of precipitation data by querying the previous 12 months of data.
3. Loaded the query results into a Pandas DataFrame. Explicitly set the column names.
4. Sorted the DataFrame values by "date".
5. Plotted the results by using the DataFrame plot method.
6. Used Pandas to print the summary statistics for the precipitation data.

# Station Analysis
1. Designed a query to calculate the total number of stations in the dataset.
2. Designed a query to find the most-active stations (that is, the stations that have the most rows).
   To do so, completed the following steps:
3. Listed the stations and observation counts in descending order.

to Answer the following question: which station id has the greatest number of observations?
Designed a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.

1. Designed a query to get the previous 12 months of temperature observation (TOBS) data. To do so, complete the following steps:
2. Filtered by the station that has the greatest number of observations.
3. Query the previous 12 months of TOBS data for that station.
4. Plotted the results as a histogram with bins=12, as the following image shows:
5. depictted the histogram.
6. Closed your session.

# Part 2: Design of Climate App
After completting the initial analysis, 
have designed a Flask API based on the queries that was just developed. 
To do so, used the Flask to create routes as follows:

1. /
   
. Startted at the homepage.
. Listed all the available routes.

2. /api/v1.0/precipitation
   
. Converted the query results from precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
. Returned the JSON representation of dictionary.

3. /api/v1.0/stations
   
. Returned a JSON list of stations from the dataset.

4. /api/v1.0/tobs
   
. Query the dates and temperature observations of the most-active station for the previous year of data.
. Returned a JSON list of temperature observations for the previous year.

5. /api/v1.0/<start> and /api/v1.0/<start>/<end>

. Returned a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
. For a specified start, calculated TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
. For a specified start date and end date, calculated TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.

# Note 
. Joinned the station and measurement tables for some of the queries.
. Used the Flask jsonify function to convert API data to a valid JSON response object.

# Repo Direction
. Created a new repository for this project called "sqlalchemy-challenge", Cloned the new repository(remote) to local by terminal.
. Inside my local Git repository, created a folder for "SurfsUp"
. Added Jupyter notebook "climate_starter.ipynb" and python script for app "app.py" to this folder. This is the main script to run this analysis.
. A Resources folder that contains the CSV files(Raw Data) and "hawaii.sqlite" i have used.
. Pushed these changes to GitHub profile by bash terminal.
