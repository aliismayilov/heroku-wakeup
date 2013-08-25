import httplib
from time import sleep

# list of hosts to keep awake
HOSTS = [
    'yugteatr.herokuapp.com',
    'bethclip.com',
    'edu-active.herokuapp.com'
]

# waiting time in seconds
TIME = 1200 # 20 minutes

def get_status_code(host, path="/"):
    try:
        conn = httplib.HTTPConnection(host)
        conn.request("HEAD", path)
        return conn.getresponse().status
    except StandardError:
        return None

while True:
    for host in HOSTS:
        print '{host} - HTTP {status}'.format(
            host=host,
            status=get_status_code(host)
        )
    # wait for a sec
    sleep(TIME)
