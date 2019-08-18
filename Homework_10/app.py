import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

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
Station = Base.classes.station
Measurement = Base.classes.station

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
        f"/api/v1.0/station" 
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


    """Return a list of all passenger names"""
    # Query all passengers
    results = session.query(Measurement.date,Measurement.prcp).filter(Measurement.date >= nd).filter(Measurement.date <= rf).all()

    session.close()

    # Convert list of tuples into normal list
    #all_prcp = list(np.ravel(results))

    return jsonify(results)


@app.route("/api/v1.0/station")
def names():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    results = session.query(Station.name).all()

    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)



    # Create a dictionary from the row data and append to a list 
    # of all_passengers
    all_passengers = []
    for station, name in results:
        passenger_dict = {}
        passenger_dict["station"] = station
        passenger_dict["name"] = name
        all_passengers.append(passenger_dict)

    return jsonify(all_passengers)


if __name__ == '__main__':
    app.run(debug=True)
