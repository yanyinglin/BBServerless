from cryptography.fernet import Fernet, MultiFernet
import time
import socket

def handler(event, context):
    startTime = time.time()

    obj = "crypt test"

    #obj = args.get("crypt", "crypt test")
    obj = bytes(obj, 'utf-8')
    key1 = Fernet(Fernet.generate_key())
    key2 = Fernet(Fernet.generate_key())
    f = MultiFernet([key1, key2])
    time_load = time.time() - startTime
    token = f.encrypt(obj)   
    
    invoke_time = event['data']['invoke_time']  
    result = {"token": "stream", "invoke_time":invoke_time,"startTime": startTime,"time_load": time_load,"endTime": time.time(), "runtime": time.time()-startTime, "ip":socket.gethostbyname(socket.gethostname())}
    print(result,invoke_time)
    return result

# handler("","")
