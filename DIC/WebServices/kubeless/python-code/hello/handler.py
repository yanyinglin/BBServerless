#from helper import helper
import time
import socket

def handler(event, context):
    startTime = time.time()
    name = "stranger"
    time_load = time.time() - startTime
    greeting = "Hello from helper.py, " + name + "!"
     
    invoke_time = event['data']['invoke_time']  
    result = {"token": "stream", "invoke_time":invoke_time,"startTime": startTime,"time_load": time_load,"endTime": time.time(), "runtime": time.time()-startTime, "ip":socket.gethostbyname(socket.gethostname())}
    print(result,invoke_time)
    return result

# handler("","")
