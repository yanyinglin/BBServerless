import time
from collections import Counter
from urllib import request
import json


def handle(c):
    startTime = time.time()
    url = "http://10.10.1.121:10000/files/bbserverless/bigdata/train.txt"
    filedata = request.urlopen(url)
    Counter(filedata.read().strip().split())
    result = json.dumps({"token": "inference finished", "startTime": startTime})
    return result
