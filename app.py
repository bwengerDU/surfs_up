#Import Dependancies
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
#Add SQLAlchemy Dependencies
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
#Import flask dependencies
from flask import Flask, jsonify
#Set up the data base
engine = create_engine("sqlite:///hawaii.sqlite")
#Access SQLite
Base = automap_base()
#Reflect the database
Base.prepare(engine, reflect=True)
#Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station
#Create Python to database session link
session = Session(engine)
#Define Flask App
app = Flask(__name__)
#Define welcome route
@app.route("/")
#Create function with return statement
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')
#Creating Next Route
@app.route("/api/v1.0/precipitation")
#Create Precipitation Function for previous year and precipitation
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)
#Third route: stations
@app.route("/api/v1.0/stations")
#Create functions statement
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)
#4th route: temperature
@app.route("/api/v1.0/tobs")
#Create Functions statement
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
#Fifth Route: temp start and end dates
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
#Create functions statement
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)