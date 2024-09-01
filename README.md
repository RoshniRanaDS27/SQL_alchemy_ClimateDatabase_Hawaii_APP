# Holiday vacation in Honolulu, Hawaii
# Climate Analysis API

In this section, 
Have used Python and SQLAlchemy to do a basic climate analysis and data exploration of climate database. 
Specifically, have used SQLAlchemy ORM queries, Pandas, and Matplotlib.

This project is a Flask application designed to serve as an API for climate analysis data derived from a SQLite database. The API provides several endpoints that allow users to retrieve precipitation, station, and temperature data, as well as perform basic statistical analysis based on user-defined start and end dates. The data used in this project comes from the "hawaii.sqlite" database, which contains climate data for various weather stations in Hawaii.
(After completting the initial analysis, 
have designed a Flask API based on the queries that was just developed. 
To do so, used the Flask to create routes. )

# Background
A long holiday vacation in Honolulu, Hawaii. 
To help with trip planning, have decided to do a climate analysis about the area. 
The following sections outline the steps that are considered to take to accomplish this task.
Task was broken down into the following tasks:

## Prerequisites
Before running the application, ensure that you have the following dependencies installed:

- Python 3.x
- Flask
- SQLAlchemy
- Pandas
- Matplotlib
- NumPy
- You can install the necessary Python packages using pip:
![image](https://github.com/user-attachments/assets/0798353c-4562-4567-86bf-c091e66ceaa4)

# Project Structure

- app.py: This is the main Flask application file where the API routes are defined.
- Resources/hawaii.sqlite: This is the SQLite database containing climate data.
- Resources/hawaii_stations.csv: This CSV file contains information about the weather stations.
- Resources/hawaii_measurements.csv: This CSV file contains climate measurements data.

Part 1: Analyze and Explore the Climate Data, Database Setup
Part 2: Designning Climate App

# Database Setup

The application uses SQLAlchemy to connect to the SQLite database and map the database tables to Python classes. The database contains two primary tables:

- Measurement: Stores climate measurement data, including dates, precipitation levels, and temperature observations.
- Station: Stores information about the weather stations.
- ![image](https://github.com/user-attachments/assets/cbc3a9b4-5c58-47d8-ac72-8f28e9225d0d)

# Flask API Endpoints (Design of Climate App)
The Flask application provides the following API endpoints:

1. Home Route (/)
- Displays a list of all available API routes.

2. Precipitation Data (/api/v1.0/precipitation)
- Returns a JSON representation of the precipitation data for the last 12 months.

3. Station Data (/api/v1.0/stations)
- Returns a JSON list of all weather stations in the database.

4. Temperature Observations (/api/v1.0/tobs)
- Returns a JSON list of temperature observations for the most active station in the last 12 months.

5. /api/v1.0/<start> ( Temperature Statistics from Start Date)
- Returns a JSON list of minimum, average, and maximum temperatures from a given start date.

6. /api/v1.0/<start>/<end> (Temperature Statistics from Start to End Date)
- Returns a JSON list of minimum, average, and maximum temperatures for a specified date range.

# Running the Application
To start the Flask application, execute the following command:
![image](https://github.com/user-attachments/assets/4030e314-088a-4569-af96-56ed7d71445d)

By default, the application will run on 'http://127.0.0.1:5000/' . You can use any web browser or tool like Postman to access the API routes.

# Example Queries
- Precipitation Data: http://127.0.0.1:5000/api/v1.0/precipitation
- Station Data: http://127.0.0.1:5000/api/v1.0/stations
- Temperature Observations: http://127.0.0.1:5000/api/v1.0/tobs
- Temperature Stats from Start Date: http://127.0.0.1:5000/api/v1.0/2016-08-23
- Temperature Stats from Start to End Date: http://127.0.0.1:5000/api/v1.0/2016-08-23/2017-08-23

# Exploratory Data Analysis (EDA)
The project also includes Python scripts for exploratory data analysis using Pandas and Matplotlib. The EDA scripts analyze precipitation and station data, calculating statistics such as the total number of stations, the most active stations, and temperature trends over time. These analyses help in understanding the data before creating the API.

## Part 1: Analyze and Explore the Climate Data
In this section, have used Python and SQLAlchemy to do a basic climate analysis and data exploration of climate database. 
Specifically, used SQLAlchemy ORM queries, Pandas, and Matplotlib.     
To do so, complete the following steps:

Used the SQLAlchemy "create_engine()" function to connect to SQLite database.
Used the SQLAlchemy "automap_base()" function to reflect tables into classes, and then saved references to the classes named station and measurement.

Linked Python to the database by creating a SQLAlchemy session.
closed session at the end of the notebook.

# Requirements

1. Jupyter Notebook Database Connection
To receive all points, the following were completed:

- The SQLAlchemy create_engine() function was used to connect to the SQLite database.
- The SQLAlchemy automap_base() function was used to reflect the tables into classes.
- References were saved to the classes named station and measurement.
- Python was linked to the database by creating a SQLAlchemy session.
- The session was closed at the end of the notebook.

2. Precipitation Analysis
To receive all points, the following were completed:

- A query was created to find the most recent date in the dataset (8/23/2017).
- A query was created to collect only the date and precipitation for the last year of data without passing the date as a variable.
- The query results were saved to a Pandas DataFrame to create date and precipitation columns.
- The DataFrame was sorted by date.
- The results were plotted using the DataFrame plot method with date as the x and precipitation as the y variables.
- Pandas was used to print the summary statistics for the precipitation data.

3. Station Analysis
To receive all points, the following were completed:

- A query was designed to correctly find the number of stations in the dataset (9).
- A query was designed to correctly list the stations and observation counts in descending order and identify the most active station (USC00519281).
- A query was designed to find the min, max, and average temperatures for the most active station (USC00519281).
- A query was created to get the previous 12 months of temperature observation (TOBS) data filtered by the station that had the greatest number of observations.
- The query results were saved to a Pandas DataFrame.
- A histogram was correctly plotted with bins=12 for the last year of data using tobs as the column to count.

4. API SQLite Connection & Landing Page
To receive all points, the Flask application included the following:

- The engine was correctly generated to the correct SQLite file.
- automap_base() was used to reflect the database schema.
- References were correctly saved to the tables in the SQLite file (measurement and station).
- The session was correctly created and bound between the Python app and the database.
- The available routes were displayed on the landing page.

5.  API Static Routes
To receive all points, the Flask application included the following routes:

- Precipitation route:
   - Returned JSON with the date as the key and the value as the precipitation.
   - Only returned the JSONified precipitation data for the last year in the database.
- Stations route:
   - Returned JSONified data of all of the stations in the database.
- TOBS route:
   - Returned JSONified data for the most active station (USC00519281).
   - Only returned the JSONified data for the last year of data.

6. API Dynamic Routes
To receive all points, the Flask application included the following dynamic routes:

- Start route:
   - Accepted the start date as a parameter from the URL.
   - Returned the min, max, and average temperatures calculated from the given start date to the end of the dataset.

- Start/end route:
    - Accepted the start and end dates as parameters from the URL.
    - Returned the min, max, and average temperatures calculated from the given start date to the given end date.

7. Coding Conventions and Formatting
To receive all points, the code:

- Placed imports at the top of the file, just after any module comments and docstrings, and before module globals and constants.
- Named functions and variables with lowercase characters, with words separated by underscores.
- Followed DRY (Don't Repeat Yourself) principles, creating maintainable and reusable code.
- Used concise logic and creative engineering where possible.

8. Deployment
To receive all points:

- A link to a GitHub repository was Added, cloned to the local machine and containing the files.
- The command line was used to add files to the repository.
- Appropriate commit messages were included in the files.

# Note 
. Joinned the station and measurement tables for some of the queries.
. Used the Flask jsonify function to convert API data to a valid JSON response object.

# Repo Direction
. Created a new repository for this project called "sqlalchemy-challenge", Cloned the new repository(remote) to local by terminal.   
.    Inside my local Git repository, created a folder for "SurfsUp"   
.    Added Jupyter notebook "climate_starter.ipynb" and python script for app "app.py" to this folder. 
.    This is the main script to run this analysis.
.       A Resources folder that contains the CSV files(Raw Data) and "hawaii.sqlite" i have used.
.       Pushed these changes to GitHub profile by bash terminal.
