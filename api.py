import jobs.py

@app.route('/jobs', methods=['POST'])
def jobs_api():
    try:
        job = request.get_json(force=True)
    except Exception as e:
        return True, json.dumps({'status': "Error", 'message': 'Invalid JSON: {}.'.format(e)})
    return json.dumps(jobs.add_job(job['start'], job['end']))

@app.route('/kiosk/')
def get_kiosk():
    


# only call the function
#execute_job(jid):

@app.route('/print',methods=['POST'])
def print_thing():
    return "hello"
