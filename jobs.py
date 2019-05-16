from hotqueue import HotQueue
#import tkinter
import redis
import json
import uuid
import datetime
import os
import io #new line
import pandas as pd
import numpy as np
import matplotlib as plt
import app # importing api functions
from datetime import timedelta #changed dataetime to datetime
import matplotlib.pyplot as plt

# getting IP of redis
def get_redis_ip():
    return os.environ.get('REDIS_IP')

# queue
rd = redis.StrictRedis(host=get_redis_ip(),port=6379,db=0)
queue = HotQueue("queue", host=get_redis_ip(), port=6379, db=1)
# data = redis.strictRedis(host=get_redis_ip(),port=6379,db=2)
plots = redis.StrictRedis(host=get_redis_ip(),port=6379,db=3)


# get time
def current_time():
    d = timedelta(hours = -6)
    tz = datetime.timezone(d)
    return str(datetime.dataetime.now(tz))

# generating job id and key
def generate_jid():
    return str(uuid.uuid4())

def generate_job_key(jid):
    return 'job.{}'.format(jid)


# Thier instantiate job format
#def instantiate_job(jid,status,create_time,start,end,offset,limit):
#    return {'id':jid,'status':status,'start':start,'end':end,'offset':offset,'limit':limit,'create time':create_time,'last update time':create_time}


# Starting job format
def instantiate_job(jid, status, start, end):
    if type(jid) == str:
        job_dict =  {'id': jid,
                     'status': status,
                     'start': start,
                     'end': end}
    else:
        job_dict =  {'id': jid.decode('utf-8'),
                     'status': status.decode('utf-8'),
                     'start': start.decode('utf-8'),
                     'end': end.decode('utf-8')}
    return job_dict

#convert job fields
#def convert_jsonn_fields(key):
#    return { 'id' rd.hget(key,'id').decode('utf-8'), 

# Saving job to redis database
def save_job(job_key, job_dict):
    rd.hmset(job_key,job_dict)

# function to add job to queue
def queue_job(jid):
    job = queue.put(jid)

# Adding job to redis queue
def add_job(start, end, status="submitted"):
    jid = generate_jid()
    job_dict = instantiate_job(jid, status, start, end)
    save_job(job_dict)
    queue_job(jid)
    return job_dict

# not sure if it goes here
def update_job_status(jid, status):
    """Update the status of job with job id `jid` to status `status`."""
    jid, status, start, end = rd.hmget(generate_job_key(jid), 'id', 'status', 'start', 'end')
    job = _instantiate_job(jid, status, start, end)
    if job:
        job['status'] = status
        _save_job(_generate_job_key(jid), job)
    else:
        raise Exception()

    """ Comment out plotting section in 
#   Plotting

# create a bytes stream object out of some raw bytes:
bstream = io.BytesIO(some_bytes)

# do something with the stream
#bstream.write(b'abc...')

# read the raw file bytes into a python object
#file_bytes = open('/tmp/myfile.png', 'rb').read()

# set the file bytes as a key in Redis
#rd.set('key', file_bytes)

def validity_test(cat): # Tests existence of field 
    data = b_cycle()
    found = False
    for key in data: 
        if key == cat: 
            found = True
    if found == False:
        print("Error: the given field can't be found")
    return found 


# two lists of data corresponding to the x and y-axis, respectively:

# Simple plot of given field 
def plotbar(cat):
    data = b_cycle() # func def in api.py 
    found = validity_test(cat)
    if found == True:
        d = pd.read_json("B-Cycle.json")
        graph = pd.value_counts(data["Membership Type"]).plot.bar() # plotting graph
        #plt.show()                                          # graph display
        return graph                                         # returns a "graph" class 
    else: 
        return

def find_mean(cat):
    data =b_cycle()
    found = validity_test(cat)
    if found == True:
        d = pd.read_json("B-Cycle.json")
        mean =d.groupby([cat]).mean()
        return mean
    else:
        return 

def plotbydate(): 
    data = pd.read_json("B-Cycle.json")
    data = data.set_index('Checkout Date')
    

def find_range(cat):
    data = b_cycle()
    found = validity_test(cat)
    if found == True:
        d = pd.read_json("B-Cycle.json")
        rg = d.groupby([cat]).range()
# Time series 

# create the scatter plot
data = b_cycle(); 

plt.scatter(t, d)

# save to a file
plt.savefig('/tmp/myfile.png', dpi=150)

# getting plot from redis
plot = hmget('<job_id>', 'plot')"""
