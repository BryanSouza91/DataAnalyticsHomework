
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mission_to_mars")

@app.route('/')
def index():
    data = mongo.db.mission_to_mars.find_one()
    return render_template('index.html', data=data)

@app.route('/scrape')
def scrape():
    mission_to_mars = mongo.db.mission_to_mars
    data = scrape_mars.scrape()
    mission_to_mars.update({}, data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
