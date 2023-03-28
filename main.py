from flask import Flask, render_template, request, jsonify
import requests
from math import radians, cos, sin, sqrt, atan2

app = Flask(__name__)

# Initialize the database
vendors = {'vendor A': {
    "name": "ABC Recycling",
    "address": "23 Bosso Road St, Minna, Niger State",
    "latitude": 9.6146,
    "longitude": 6.3659,
    "phone": "(555) 555-1234"
}, 'vendor B': {
    "name": "CDE Recycling",
    "address": "456 Gidan kwano St, Maitumbi, Minna, Niger State",
    "latitude": 9.5900,
    "longitude": 6.5500,
    "phone": "(444) 555-1234"
}, 'vendor B': {
    "name": "FGH Recycling",
    "address": "789 Lighthouse St, Tunga, Minna, NIger State",
    "latitude": 9.5956,
    "longitude": 6.5607,
    "phone": "(333) 555-1234"
}}


@app.route('/')
def home():

  return render_template('index.html')


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


@app.route('/', methods=['POST'])
def search():
    lat = request.form['latitude']
    lon = request.form['longitude']
    closest_vendors = get_closest_vendor(lat, lon, vendors)
    return render_template('index.html', closest_vendor=closest_vendors, vendors=vendors)


if __name__ == '__main__':
    app.run()

