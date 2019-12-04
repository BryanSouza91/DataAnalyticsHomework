import numpy as np
import os
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify



# Setup Database

path = os.path.join("Resources","hawaii.sqlite")
engine = create_engine(f"sqlite:///{path}")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Station = Base.classes.station
Measurement = Base.classes.measurement


# Setup Flask 

app = Flask(__name__)



# Define Flask Routes


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/'start'<br/>"
        f"/api/v1.0/'start'/'end'"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all precipitation"""
    # Query all precipitation
    results = session.query(Measurement.date,Measurement.prcp).order_by(Measurement.date).all()

    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of stations data"""
    # Query all stations
    results = session.query(*Station.__table__.columns).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_stations
    all_stations = []
    for id, station, name, latitude, longitude, elevation in results:
        station_dict = {}
        station_dict["id"] = id
        station_dict["station"] = station
        station_dict["name"] = name
        station_dict["latitude"] = latitude
        station_dict["longitude"] = longitude
        station_dict["elevation"] = elevation
        all_stations.append(station_dict)

    return jsonify(all_stations)


@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all tobs"""
    # Query all tobs
    results = session.query(Measurement.date,Measurement.tobs).filter(Measurement.date >= '2016-08-23').order_by(Measurement.date).all()

    session.close()

    # Convert list of tuples into normal list
    all_tobs = list(np.ravel(results))

    return jsonify(all_tobs)




@app.route("/api/v1.0/<start>")
def start_date(start):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
        
    tmin = session.query(func.min(Measurement.tobs)).\
        filter(Measurement.date >= start).all()[0][0]
    tavg = session.query(func.Round(func.avg(Measurement.tobs),1)).\
        filter(Measurement.date >= start).all()[0][0]
    tmax = session.query(func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all()[0][0]

    session.close()

    # Convert list of tuples into normal list
    start_temps = (tmin,tavg,tmax)

    return jsonify(start_temps)



@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
        
    tmin = session.query(func.min(Measurement.tobs)).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()[0][0]
    tavg = session.query(func.Round(func.avg(Measurement.tobs),1)).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()[0][0]
    tmax = session.query(func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()[0][0]

    session.close()

    # Convert list of tuples into normal list
    start_end_temps = (tmin,tavg,tmax)

    return jsonify(start_end_temps)



if __name__ == '__main__':
    app.run(debug=True)
