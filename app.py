from flask import Flask, jsonify, request
import json
#from jobs import jobs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from flask import send_file
from jobs import *

# The main Flask app --------------------------------
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


# Data from a json file -----------------------------
data = json.load(open('B-Cycle.json', 'r'))

############### Basic Return Functions ################

# Data return _______________________________________

@app.route('/', methods=['GET'])
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

# Getting file plots ________________________________

# inside your flask function:
@app.route('/jobs/<int:job_id>/plot', methods=['GET'])
def get_job_plot(job_id):

    # do something to get the plot from the database:
    plot = get_job_plot_from_db(job_id)
    return send_file(io.BytesIO(plot),
                     mimetype='image/png',
                     as_attachment=True,
                     attachment_filename='{}.png'.format(job_id))

@app.route('/entry/<int:id>', methods=['GET'])
def get_entry(id):

    return jsonify(data[id])
# Membership Type ____________________________________
@app.route('/membership', methods=['GET']) # Lists all Membership
def get_membership():
    membership = [x['Membership Type'] for x in data]
    membership = list(set(membership))
    return jsonify(membership)

#def get_memberships():
 #   return jsonify(data['Membership Type'])


@app.route('/membership/<int:id>', methods=['GET']) # Returns Membership of specific trip 
def get_membership_by_id(id):
    return jsonify(data['Membership Type'][id])

# Bicycle ID _________________________________________
@app.route('/bicycle', methods=['GET'])    # Lists all BIKE IDs
def get_bids():
    bicycle = [x['Bicycle ID'] for x in data]
    bicycle = list(set(bicycle))
    return jsonify(bicycle)
    

@app.route('/bicycle/<int:id>',methods=['GET']) # BIKe id of specifc trip 
def get_bid(id):
    return jsonify(data[id]['Bicycle ID'])

# Bike Check out  ____________________________________

@app.route('/cokiosk', methods=['GET']) # NAMEs 
def get_cokiosks():
    cokiosk = [x['Checkout Kiosk'] for x in data]
    cokiosk = list(set(cokiosk))
    return jsonify(cokiosk)

@app.route('/codate', methods=['GET']) # dates 
def get_dates():
    dates = [x['Checkout Kiosk'] for x in data]
    dates = list(set(dates))
    return jsonify(dates)

@app.route('/cokiosk/<int:id>', methods=['GET']) # Kiosk Name of specific trip 
def get_cokiosk():
    return jsonify(data['Checkout Kiosk'][id])

@app.route('/cokiosk/id/<int:id>', methods=['GET']) # KIOSK ID of specific trip 
def get_cokioskid(id):
    return jsonify(data['Checkout Kiosk ID'][id])

@app.route('/cokiosk/<int:id>/date', methods=['GET']) # Checkout date of specific trip 
def get_cokioskdate(id):
    return jsonify(data['Checkout Date'][id])

@app.route('/cokiosk/time', methods=['GET']) # Checkout times
def get_cokiosktimes():
    checkout_time = [x['Checkout Time'] for x in data]
    checkout_time = list(set(checkout_time))
    return jsonify(checkout_time)

@app.route('/cokiosk/time/<int:id>', methods=['GET']) # Checkout time for specific trip 
def get_cokiosktime(id):
    return jsonify(data['Checkout Time'][id])

# Bike Return  _______________________________________

@app.route('/rkiosk', methods=['GET']) #  Names  
def get_returnkiosks():
    return_kiosk = [x['Return Kiosk'] for x in data]
    return_kiosk = list(set(return_kiosk))
    return jsonify(return_kiosk)

@app.route('/rkiosk/name/<int:id>', methods=['GET']) # Name of Kiosk 
def get_returnkiosk(id):
    return jsonify(data['Return Kiosk'][id])

@app.route('/rkiosk/id', methods=['GET']) # IDs 
def get_rkioskids():
    return jsonify(data['Return Kiosk ID'])

@app.route('/rkiosk/id/<int:id>',methods=['GET']) # ID of Kiosk 
def get_rkioskid(id):
    return jsonify(data['Return Kiosk ID'][id])

# Trip Duration ______________________________________

@app.route('/duration', methods=['GET']) # Durations of trips
def get_durations(): 
    trip_duration = [x['Trip Duration Minutes'] for x in data]
    trip_duration = list(set(trip_duration))
    return jsonify(trip_duration)

@app.route('/duration/<int:id>') # Duration of specifc trip 
def get_durationid(id):
    return jsonify(data['Trip Duration Minutes'][id])

################ Data Analysis ############################


# Time Averaging -------------------------------------

@app.route('/average_time', methods=['GET'])
def get_avtime():
    # average time calculation 
    return jsonify(data['Trip Duration Minutes'][id])

@app.route('/average_time/<string:date_interval>', methods=['GET'])
def get_avtime_date():
    temp_data = pd.read_json('B-Cycle.json')
    return jsonify(temp_data['Trip Duration Minutes'].mean())

@app.route('/plot/<string:name>', methods=['GET'])
    graph(name)

#def graph(name):
#        d = pd.DataFrame.from_dict(data)
#        name = name.replace('-',' ')
#        graph = pd.value_counts(d[name]).plot.bar() # plotting graph   
#        plt.show(graph)                                       # graph displayvh
#        return '',200

