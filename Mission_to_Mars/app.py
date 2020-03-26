from flask import flask, render_template, redirect
from flask_pymongo import flask_pymongo

# Importing scrape_mars code

app = Flask(__name__)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Set database 

db = client.mars_db


@app.route("/")
def home():
    mars_results = db.mars_results.find()
    return render_template("index.html", mars_results=mars_results)


@app.route("/scrape")
def scrape():
    # drop any data that is in the db
    db.mars_results.drop()
    mars_data = scrape_mars.scrape()

    db.mars_results.insert_one(mars_data)

    # Using Flask' redirect function

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)