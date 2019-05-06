import jobs.py
import datetime
import json


@queue.worker
def execute_job(jid):
    #update status of job pending
    update_job_status(jid,'Pending')
    
    #execute job
    job = queue.get() # fix later
    time.sleep(5)
    
    #update statue of job complete
    update_json_statue(jid,'Complete')


