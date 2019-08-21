import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import pandas as pd
import time
import datetime
from datetime import timedelta
from datetime import datetime

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"        
        f"/api/v1.0/station<br/>" 
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/< date ><br/>"
        f"/api/v1.0/< start_date >/< end_date ><br/>"
        f"All dates entered in YYYY-MM-DD format, ex 2016-02-07"
   )

@app.route("/api/v1.0/precipitation")
def prcp():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    end_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    last_date = end_date[0]
    rf = datetime.strptime(last_date, '%Y-%m-%d').date()
    rng_start_date = rf - timedelta(days=365)
    sd = str(rng_start_date)
    nd = rf - timedelta(days=365)
    #results = end_date
  
 
    # Query
    results = session.query(Measurement.date,Measurement.prcp).filter(Measurement.date >= nd).filter(Measurement.date <= rf).all()

    session.close()

    # Convert list of tuples into normal list
    all_prcp = list(np.ravel(results))

    return jsonify(results)


@app.route("/api/v1.0/station")
def names():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all station names"""
    # Query all stations
    results = session.query(Station.name).all()

    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(results)

    

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    end_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    last_date = end_date[0]
    rf = datetime.strptime(last_date, '%Y-%m-%d').date()
    rng_start_date = rf - timedelta(days=365)
    sd = str(rng_start_date)
    nd = rf - timedelta(days=365)
    #results = end_date
  
    # Query 
    results = session.query(Measurement.date,Measurement.tobs).filter(Measurement.date >= nd).filter(Measurement.date <= rf).all()

    session.close()

    # Convert list of tuples into normal list
    all_tobs = list(np.ravel(results))

    return jsonify(results)

@app.route("/api/v1.0/<string:start_date>")
def day_temps(start_date):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # This function called `calc_temps` will accept start date and end date in the format '%Y-%m-%d' 
# and return the minimum, average, and maximum temperatures for that range of dates
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date == start_date).all()

    session.close()

    # Convert list of tuples into normal list
    all_calc_temps = list(np.ravel(results))

    return jsonify(results)


@app.route("/api/v1.0/<string:start_date>/<string:end_date>")
def calc_temps(start_date, end_date):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # This function called `calc_temps` will accept start date and end date in the format '%Y-%m-%d' 
# and return the minimum, average, and maximum temperatures for that range of dates
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

    session.close()

    # Convert list of tuples into normal list
    all_calc_temps = list(np.ravel(results))

    return jsonify(results)












if __name__ == '__main__':
    app.run(debug=True)
