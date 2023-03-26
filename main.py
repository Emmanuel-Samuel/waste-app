from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])



@app.route('/', methods=['GET', 'POST'])
def vendors():
        address = request.form['address']
        url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={}&radius=50000&type=solar_panel&key=YOUR_API_KEY'.format(address)
        response = requests.get(url)
        data = json.loads(response.text)
        vendors = []
        for result in data['results']:
            vendor = {}
            vendor['name'] = result['name']
            vendor['address'] = result['vicinity']
            vendor['contact'] = result['contact']
            vendors.append(vendor)
        return render_template('index.html', vendors)

app.run('')