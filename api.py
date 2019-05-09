from flask import Flask, jsonify, request
import json
import jobs.py

# The main Flask app --------------------------------
app = Flask(__name__)

# Data from a json file -----------------------------
data = json.load(open('B-Cycle', 'r'))

# Data return _______________________________________

@app.route('/', method=['GET'])
def b_cycle():
    return jsonify(data)

# Jobs ______________________________________________

@app.route('/jobs', methods=['POST'])
def jobs_api():
    try:
        job = request.get_json(force=True)
    except Exception as e:
        return True, json.dumps({'status': "Error", 'message': 'Invalid JSON: {}.'.format(e)})
    return json.dumps(jobs.add_job(job['start'], job['end']))

# Membership Type ____________________________________
@app.route('/membership',method=['GET']) # Lists all Membership
def get_membership():
    return jsonify(data['Membership Type'])

@app.route('/membership/<int:id>',method=['GET']) # Returns Membership of specific trip 
def get_membershipid(id):
    return jsonify(data['Membership Type'][id])

# Bicycle ID _________________________________________
@app.route('/bicycle',method=['GET'])    # Lists all BIKE IDs
def get_bid():
    return jsonify(data['Bicycle ID'])

@app.route('/bicycle/<int:id>',method=['GET']) # Lists BIKe id of specifc trip 
def get_bidtid(id);
    return jsonify(data['Bicycle ID'][id])

# Bike Check out  ____________________________________

@app.route('/cokiosk/', method=['GET']) # NAMEs 
def get_cokiosk():
    return jsonify(data['Checkout Kiosk'])

@app.route('/cokiosk/id', method=['GET']) # KIOSK IDs 
def get_cokioskid():
    return jsonify(data['Checkout Kiosk ID'])

@app.route('/cokiosk/<kid>/date', method=['GET']) # DATEs
def get_cokioskdate(id):
    return jsonify(data['Checkout Date'])

@app.route('/cokiosk/<kid>/<date>'')

# Bike Return  _______________________________________

@app.route('/rkiosk/', method=['GET']) #  Name  
def get_cikiosk():
    return jsonify(data['Return Kiosk'])

@app.route('/rkiosk/<kioskid>', method=['GET']) # ID 
def get_cikioskid():
    return jsonify(data['Return Kiosk ID'])

@app.route('/rkiosk/<kioskid>/<date>', method=['GET'])
def get_cikioskdate():


# Trip Duration ______________________________________
@app.route('/duration',method=['GET'])
def get_duration(): 
    return jsonify(data['Trip Duration Minutes'])

@app.route('/duration/<int:id>')
def get_durationid(id):
    return jsonify(data[id]['Trip Duration Minutes'])


# Time Averaging -------------------------------------

@app.route('/average_time', method=['GET'])
def get_avtime():

@app.route('/average_time/<date_interval>', method=['GET'])
def get_avtime_date():
