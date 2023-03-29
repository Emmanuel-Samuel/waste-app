"""
    This app will use Google GeoLocationAPI, Spreadsheet, SQL Database.
    With difficulties getting a biling account to access the api service,
    we decided to, improvise. Created a database in form of a dictionary,
    using python dictionary(Google SQL Database). Ask user to input for latitude
    and longitude instead of getting it using(Google Geolocation). Read form
    input to a txt file instead of a (Google Spreadsheet)
    This codes below are for implementing the google services, they will be commented out
    since they are not used yet.
"""
"""
  # Google Geolocation API key
    GEOLOCATION_API_KEY = 'your_api_key_here'

  # Connect to MySQL database
  db = mysql.connector.connect(
      host="localhost",
      user="yourusername",
      password="yourpassword",
      database="yourdatabase"
  )

  # Function to get the user's location using the Google Geolocation API
  def get_user_location():
    url = 'https://www.googleapis.com/geolocation/v1/geolocate?key=' + GEOLOCATION_API_KEY
    response = requests.post(url)
    location = response.json()['location']
    return (location['lat'], location['lng'])

  # Query database to get vendors
        cursor = db.cursor()
        cursor.execute("SELECT * FROM vendors")
        vendors = cursor.fetchall()
  
  # for working with google spreadsheet
    import gspread
    # gets spreadsheet and establishes connection to google
    gc = gspread.service_account('secrets.json')
    # gets worksheet
    spreadsheet = gc.open('{input name of spreadsheet}') 
    # sample on updating spreadsheet
    worksheet.update_cell(row, column, value)
"""


# import modules
from flask import Flask, render_template, request, jsonify
import requests
from math import radians, cos, sin, sqrt, atan2
import pandas as pd


# creates an app instance
app = Flask(__name__)


# Initialize the database as a dictionary
vendors = {'vendor A': {
    "name": "ABC Recycling",
    "address": "23 Bosso Road St, Minna, Niger State",
    "latitude": 10.6146,
    "longitude": 13.3659,
    "phone": "(555) 555-1234"
}, 'vendor B': {
    "name": "CDE Recycling",
    "address": "456 Gidan kwano St, Maitumbi, Minna, Niger State",
    "latitude": 20.5900,
    "longitude": 26.5500,
    "phone": "(444) 555-1234"
}, 'vendor B': {
    "name": "FGH Recycling",
    "address": "789 Lighthouse St, Tunga, Minna, NIger State",
    "latitude": 9.5956,
    "longitude": 6.5607,
    "phone": "(333) 555-1234"
}}


# renders the homepage
@app.route('/')
def home():

  return render_template('index.html')


# function for calculating distance between user and vendor points using lat, lon as inputs
def get_closest_vendor(user_lat, user_lon, vendors=vendors):
    closest_vendor = None
    closest_distance = float('inf')

    # Loop through each vendor in the database
    for vendor_name, vendor_info in vendors.items():
        # Calculate the distance between the user and the vendor using the Haversine formula
        vendor_lat = vendor_info['latitude']
        vendor_lon = vendor_info['longitude']
        dlat = radians(vendor_lat - float(user_lat))
        dlon = radians(vendor_lon - float(user_lon))
        a = sin(dlat / 2) ** 2 + cos(radians(float(user_lat))) * cos(
            radians(vendor_lat)) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = 6371 * c  # Radius of the earth in km

        # If the current vendor is closer than the previous closest vendor, update the variables
        if distance < closest_distance:
            closest_distance = distance
            closest_vendor = {"name": vendor_info["name"],
                              "address": vendor_info["address"],
                              "phone": vendor_info["phone"]}

    # Return the closest vendor's information as a dictionary
    return closest_vendor



# renders the search query results
@app.route('/', methods=['POST'])
def search():
    lat = request.form['latitude']
    lon = request.form['longitude']
    closest_vendors = get_closest_vendor(lat, lon, vendors)

    return render_template('index.html', closest_vendor=closest_vendors, vendors=vendors)


@app.route('/', methods=['POST'])
def submit():
    # gets input from user
    name = request.form['name']
    email = request.form['email']
    address = request.form['address']
    waste_type = request.form['subject']
    desc_msg = request.form['message']

    submit_msg = 'Submitted'
    # returns the message
    return render_template('index.html', submitted=submit_msg)


# runs the app
if __name__ == '__main__':
    app.run(host="0.0.0.0")

