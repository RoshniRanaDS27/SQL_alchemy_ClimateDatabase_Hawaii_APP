# Import the dependencies.
import sqlalchemy
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import numpy as np
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with = engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
# Define routes below

@app.route('/')
def home():
    'List all available API routes.'
    return (
        f'Welcome to Climate App<br/>'
        f'Available Routes:<br/>'
        f'/api/v1.0/precipitation<br/>'
        f'/api/v1.0/stations<br/>'
        f'/api/v1.0/tobs<br/>'
        f'/api/v1.0/&lt;start&gt; (replace &lt;start&gt; with start date in yyyy-mm-dd format)<br/>'
        f'/api/v1.0/&lt;start&gt;/&lt;end&gt; (replace &lt;start&gt; and &lt;end&gt; with start and end dates in yyyy-mm-dd format)<br/>'

    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the JSON representation of precipitation data for the last 12 months."""
  
    # Calculate the date one year ago from today
    one_year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Query to retrieve the last 12 months of precipitation data
    precipitation_data = session.query(Measurement.date, Measurement.prcp).\
                          filter(Measurement.date >= one_year_ago).all()
    
    # Convert the query results to a dictionary
    precipitation_dict = {date: prcp for date, prcp in precipitation_data}

 # Add a title to the dictionary
    title = "Precipitation Data for the Last 12 Months"
    result_dict = {"title": title, "data": precipitation_dict}

    return jsonify(result_dict)

# Define route to stations
@app.route("/api/v1.0/stations")
def stations():

    # Query to retrieve stations
    stations = session.query(Station.station, Station.name).all()
    
    # Convert the query results to a dictionaries
    station_lists = [{"station": station, "name": name} for station, name in stations]
    
    return jsonify(station_lists)

@app.route("/api/v1.0/tobs")
def tobs():
    # Find the most active station
    most_active_station = session.query(Measurement.station, func.count(Measurement.station)).\
                           group_by(Measurement.station).\
                           order_by(func.count(Measurement.station).desc()).first()[0]
    
    # Calculate the date one year ago from today
    one_year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Query to retrieve temperature observations for the most active station for the last year
    tobs_data = session.query(Measurement.date, Measurement.tobs).\
                filter(Measurement.station == most_active_station).\
                filter(Measurement.date >= one_year_ago).all()
    
    # Convert the query results to a dictionary
    tobs_dict_list = {date: tobs for date, tobs in tobs_data}
    
    return jsonify(tobs_dict_list)

@app.route("/api/v1.0/<start>")
def start_date(start):

    # Convert start date string to datetime
    start_date = dt.datetime.strptime(start,'%Y-%m-%d').date()
    
    # Query to retrieve temperature statistics for dates greater than or equal to the start date
    temp_stats = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                 filter(Measurement.date >= start_date).all()
    
     # Convert the query results to a dictionary with titles
    result_dict = {
        "start_date": start_date.strftime('%Y-%m-%d'),
        "end_date": end_date.strftime('%Y-%m-%d'),
        "min_temperature": temp_stats[0][0],
        "avg_temperature": temp_stats[0][1],
        "max_temperature": temp_stats[0][2]
    }
    
    # Convert the query results to a list
    temp_stats_lists = list(np.ravel(result_dict))

     # Add a title to the response
    title = "Temperature Statistics from Start Date"
    response = {"title": title, "start_date": start, "temperature_statistics": temp_stats_lists}
    
    return jsonify(response)

@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):

    # Convert start and end date strings to datetime objects
    start_date = dt.datetime.strptime(start,'%Y-%m-%d').date()
    end_date = dt.datetime.strptime(end,'%Y-%m-%d').date()
    
    # Query to retrieve temperature statistics for dates between the start and end dates
    temp_stats = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                 filter(Measurement.date >= start_date).\
                 filter(Measurement.date <= end_date).all()
    
     # Convert the query results to a dictionary with titles
    result_dict = {
        "start_date": start_date.strftime('%Y-%m-%d'),
        "end_date": end_date.strftime('%Y-%m-%d'),
        "min_temperature": temp_stats[0][0],
        "avg_temperature": temp_stats[0][1],
        "max_temperature": temp_stats[0][2]
    }
    
    # Convert the query results to a list
    temp_stats_lists = list(np.ravel(result_dict))

    # Add a title to the response
    title = "Temperature Statistics from Start Date to End Date"
    response = {"title": title, "start_date": start, "end_date": end, "temperature_statistics": temp_stats_lists}
    
    return jsonify(temp_stats_lists)

# Add more routes and functionalities as needed

if __name__ == '__main__':
    app.run(debug=True)
