#Import dependencies/tools
from flask import Flask, render_tempelate, redirect, url_for
from flask_pymongo import PyMongo
import scraping

#Set up flask
app = Flask(__name__)

#Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#define the route for the HTML page
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_tempelate("index.html", mars=mars)

#Add next route and function
@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scraping.scrape_all()
    mars.update({}, mars_data, upsert=True)
    return redirect('/', code 302)

#Tell flask to run
if __name__ == "__main__":
    app.run()