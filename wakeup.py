import httplib

# list of hosts to keep awake
hosts = [
    'yugteatr.herokuapp.com'
]

def get_status_code(host, path="/"):
    try:
        conn = httplib.HTTPConnection(host)
        conn.request("HEAD", path)
        return conn.getresponse().status
    except StandardError:
        return None

for host in hosts:
    print '{host} - HTTP {status}'.format(
        host=host,
        status=get_status_code(host)
    )
