
import datetime
import logging
import sys
from dateutil.tz import tzlocal
from flask import Flask, request

# We'll do our own logging, thanks
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    write("[{:%Y-%m-%d %H:%M:%S %z}] {} {}".format(datetime.datetime.now(tzlocal()), request.method, request.url))
    printTable({k: repr(v) for k, v in request.headers.items()}, "Header", "Value", prefix="\t")
    data = request.get_data()
    if len(data) == 0:
        write("No request body")
    else:
        write("Request data:")
        write("\t" + repr(data))
    return "OK\n"

def printTable(tab, keyname, valuename, prefix=""):
    klen = max(len(keyname), max(len(x) for x in tab.keys()))
    vlen = max(len(valuename), max(len(x) for x in tab.values()))
    fmt = prefix + "%%- %ds : %%- %ds" % (klen, vlen)
    write(fmt % (keyname, valuename))
    write(prefix +  ('=' * (klen + vlen + 3)))
    for k in sorted(tab.keys()):
        write(fmt % (k, tab[k]))

def write(*lst, **kw):
    kwargs = {'file': sys.stderr}
    kwargs.update(kw)
    return print(*lst, **kwargs)

if __name__ == '__main__':
    write("Starting server on 0.0.0.0:5000")
    app.run(host='0.0.0.0')
