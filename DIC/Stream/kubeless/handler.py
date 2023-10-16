from collections import Counter
import socket
import time
from urllib import request
import json

def handler(event, context):
    startTime = time.time()
    url = 'http://10.10.1.121:10000/files/stream_data/{i}'.format(i=32)
    filedata = request.urlopen(url)
    time_load = time.time() - startTime
    
    Counter(filedata.read().strip().split())
    # print(type(event))
    invoke_time = event['data']['invoke_time']
    
    result = {"token": "stream", "invoke_time":invoke_time,"startTime": startTime,"time_load": time_load,"endTime": time.time(), "runtime": time.time()-startTime, "ip":socket.gethostbyname(socket.gethostname())}
    print(result,invoke_time)
    return result

# handler("","")
