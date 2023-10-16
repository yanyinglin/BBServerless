import hashlib
import os
import time
import socket

def handler(event, context):
    global token
    startTime = time.time()
    md5_obj = hashlib.md5()
    md5_obj.update(b"user_name.....")
    time_load = time.time() - startTime
    hash_code = md5_obj.hexdigest()
    token = str(hash_code).lower()
     
    invoke_time = event['data']['invoke_time']  
    result = {"token": "stream", "invoke_time":invoke_time,"startTime": startTime,"time_load": time_load,"endTime": time.time(), "runtime": time.time()-startTime, "ip":socket.gethostbyname(socket.gethostname())}
    print(result,invoke_time)
    return result

# handler("","")