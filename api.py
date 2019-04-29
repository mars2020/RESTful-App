import jobs.py

@api.route('/jobs', methods=['POST'])
def jobs_api():
    try:
        job = request.get_json(force=True)
    except Exception as e:
        return True, json.dumps({'status': "Error", 'message': 'Invalid JSON: {}.'.format(e)})
    return json.dumps(jobs.add_job(job['start'], job['end']))

# only call the function
#@......
#def execute_job(jid):
#    ......

@api.route('/print',methods=['POST'])
def print_thing():
    return "hello"
