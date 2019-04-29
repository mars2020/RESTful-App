from hotqueue import HotQueue
import redis

# redis server connection
rd = redis.StrictRedis(host='172.17.0.1', port=6379, db=0)


# generating job id and key
def generate_jid():
    return str(uuid.uuid4())

def generate_job_key(jid):
    return 'job.{}'.format(jid)

# queue
q = HotQueue("queue", host='172.17.0.1', port=6379, db=1)


def instantiate_job(jid, status, start, end):
    if type(jid) == str:
        return {'id': jid,
                'status': status,
                'start': start,
                'end': end
        }
    return {'id': jid.decode('utf-8'),
            'status': status.decode('utf-8'),
            'start': start.decode('utf-8'),
            'end': end.decode('utf-8')
    }


def save_job(job_key, job_dict):
    """Save a job object in the Redis database."""
    rd.hmset(.......)

def queue_job(jid):
    """Add a job to the redis queue."""
    ....
def add_job(start, end, status="submitted"):
    """Add a job to the redis queue."""
    jid = generate_jid()
    job_dict = instantiate_job(jid, status, start, end)
    save_job(......)
    queue_job(......)
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

