import time
import json
import torch
import socket

def handler(event, context):
    startTime = time.time()
    model= torch.load('./model/shufflenet.pt')
    time_load = time.time() - startTime
    # model.load_state_dict(torch.load('/home/app/function/model/mobilenet.pkl'))
    # model= torch.load('./model/shufflenet.pt')
    x = torch.randn(32,3,32,32)
    y = model(x)
    
    m = torch.nn.functional.softmax(y[0], dim=0)
    end_time = time.time()
    # print(m)
     
    invoke_time = event['data']['invoke_time']  
    result = {"token": "stream", "invoke_time":invoke_time,"startTime": startTime,"time_load": time_load,"endTime": time.time(), "runtime": time.time()-startTime, "ip":socket.gethostbyname(socket.gethostname())}
    print(result,invoke_time)
    return result

# handler(None)