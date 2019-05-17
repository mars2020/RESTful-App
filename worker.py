from jobs import *
import datetime
import json
from app import *
from hotqueue import HotQueue

d = pd.read_json(b_cycle())  

@queue.worker
def execute_job(jid):
    #update status of job pending
    update_job_status(jid,'Pending')
    
    #execute job
    job = queue.get() # fix later
    time.sleep(5)

def graph(name):       
    name = name.replace('-',' ')
    graph = pd.value_counts(d[name]).plot.bar() # plotting graph
    plt.show(graph)                                       # graph display
    return '',200

    #update statue of job complete
    update_json_statue(jid,'Complete')

def summary(name)
   
    name = name.replace('-',' ')
    if name = "Checkout Date"
    m = {
        "field" : name,
        "mean" : pd.d[name].mean(),
        "Median" : pd.d[name].median(),
        "Mode" : pd.d[name].mode(), 
        "SD" : pd.d[name].std(), 
        "Range" : ,
    }

