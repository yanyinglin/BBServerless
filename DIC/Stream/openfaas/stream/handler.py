import time
from collections import Counter
from urllib import request
import random
import json


def handle(c):
    startTime = time.time()
    url = "http://10.10.1.121:10000/files/stream_data/600KB/{i}".format(
        i=random.randint(1, 10)
    )
    filedata = request.urlopen(url)
    Counter(filedata.read().strip().split())
    # for key, value in count.most_common(100):
    #     print(key + " - " + str(value))
    return json.dumps({"token": "inference finished", "startTime": startTime})
