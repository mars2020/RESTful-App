from jobs import *
import datetime
import json
from app import *
from hotqueue import HotQueue

data = json.load(open('B-Cycle.json', 'r'))   

@queue.worker
def execute_job(jid):
    #update status of job pending
    update_job_status(jid,'Pending')
    
    #execute job
    job = queue.get() # fix later
    time.sleep(5)

def graph(name):
    d = app.b_cycle()
    name = name.replace('-',' ')
    graph = pd.value_counts(d[name]).plot.bar() # plotting graph
    plt.show(graph)                                       # graph displayvh
    return '',200

    #update statue of job complete
    update_json_statue(jid,'Complete')


