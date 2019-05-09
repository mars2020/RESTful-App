from flask import Flask, jsonify, request
import json
import jobs.py

# The main Flask app
app = Flask(__name__)

# Data from a json file
data = json.load(open('B-Cycle', 'r'))

@app.route('/', method=['GET'])
def b_cycle():
    return jsonify(data)

@app.route('/jobs', methods=['POST'])
def jobs_api():
    try:
        job = request.get_json(force=True)
    except Exception as e:
        return True, json.dumps({'status': "Error", 'message': 'Invalid JSON: {}.'.format(e)})
    return json.dumps(jobs.add_job(job['start'], job['end']))

@app.route('/kiosk/')
def get_kiosk():
    
@app.route('/kiosk/<kioskid>')
def get_kioskid():

@app.route('/kiosk/<kioskid>/<date>')
def get_kioskdate():

@app.route('/average_time')
def get_avtime():

@app.route('/average_time/<date_interval>')
def get_avtime_date():


# only call the function
#execute_job(jid):

@app.route('/print',methods=['GET'])
def print_thing():
    return "hello"

@app.route('/')
