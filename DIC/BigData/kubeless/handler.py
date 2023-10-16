import time
from collections import Counter
from urllib import request
import socket
import json

def handler(event, context):
    startTime = time.time()
    url = 'http://172.169.8.254:10000/files/bbserverless/bigdata/train.txt'
    filedata = request.urlopen(url)
    time_load = time.time() - startTime
    count = Counter(filedata.read().strip().split())
    
    invoke_time = event['data']['invoke_time']
    result = {"token": "stream", "invoke_time":invoke_time,"startTime": startTime,"time_load": time_load,"endTime": time.time(), "runtime": time.time()-startTime, "ip":socket.gethostbyname(socket.gethostname())}
    print(result,invoke_time)
    return result


# handler("","")