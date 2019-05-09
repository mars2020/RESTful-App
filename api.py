from flask import Flask, jsonify, request
import json
import jobs.py

# The main Flask app --------------------------------
app = Flask(__name__)

# Data from a json file -----------------------------
data = json.load(open('B-Cycle', 'r'))

############### Basic Return Functions ################

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
def get_memberships():
    return jsonify(data['Membership Type'])

@app.route('/membership/<int:id>',method=['GET']) # Returns Membership of specific trip 
def get_membership(id):
    return jsonify(data['Membership Type'][id])

# Bicycle ID _________________________________________
@app.route('/bicycle',method=['GET'])    # Lists all BIKE IDs
def get_bids():
    return jsonify(data['Bicycle ID'])

@app.route('/bicycle/<int:id>',method=['GET']) # Lists BIKe id of specifc trip 
def get_bid(id);
    return jsonify(data['Bicycle ID'][id])

# Bike Check out  ____________________________________

@app.route('/cokiosk/', method=['GET']) # NAMEs 
def get_cokiosks():
    return jsonify(data['Checkout Kiosk'])

@app.route('/cokiosk/<int:id>',method=['GET']) # Kiosk Name of specific trip 
def get_cokiosk():
    return jsonify(data['Checkout Kiosk'][id])

@app.route('/cokiosk/id', method=['GET']) # KIOSK IDs 
def get_cokioskids():
    return jsonify(data['Checkout Kiosk ID'])

@app.route('/cokiosk/id/<int:id>',method=['GET']) # KIOSK ID of specific trip 
def get_cokioskid(id):
    return jsonify(data['Checkout Kiosk ID'][id])

@app.route('/cokiosk/date', method=['GET']) # Checkout dates
def get_cokioskdates():
    return jsonify(data['Checkout Date'])

@app.route('/cokiosk/<int:id>/date', method=['GET']) # Checkout date of specific trip 
def get_cokioskdate(id):
    return jsonify(data['Checkout Date'][id])

<<<<<<< HEAD
@app.route('/cokiosk/time',method=['GET']) # Checkout times
def get_cokiosktimes():
    return jsonify(data['Checkout Time'])

@app.route('/cokiosk/time/<int:id>',method=['GET']) # Checkout time for specific trip 
def get_cokiosktime(id):
    return jsonify(data['Checkout Time'][id])

=======
>>>>>>> e3b6e42dcbdf68421205577be8a92c5c9dd4d62e
# Bike Return  _______________________________________

@app.route('/rkiosk/name', method=['GET']) #  Names  
def get_returnkiosks():
    return jsonify(data['Return Kiosk'])

@app.route('/rkiosk/name/<int:id>',method=['GET']) # Name of Kiosk 
def get_returnkiosk(id):
    return jsonify(data['Return Kiosk'][id])

@app.route('/rkiosk/id', method=['GET']) # IDs 
def get_rkioskids():
    return jsonify(data['Return Kiosk ID'])

@app.route('/rkiosk/id/<int:id>',method=['GET']) # ID of Kiosk 
def get_rkioskid(id):
    retrun jsonify(data['Return Kiosk ID'][id])

# Trip Duration ______________________________________

@app.route('/duration',method=['GET']) # Durations of trips
def get_durations(): 
    return jsonify(data['Trip Duration Minutes'])

@app.route('/duration/<int:id>') # Duration of specifc trip 
def get_durationid(id):
    return jsonify(data['Trip Duration Minutes'][id])

################ Data Analysis ############################


# Time Averaging -------------------------------------

@app.route('/average_time', method=['GET'])
def get_avtime():

@app.route('/average_time/<date_interval>', method=['GET'])
def get_avtime_date():
