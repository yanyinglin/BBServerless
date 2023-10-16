import time
import json
import torch
import socket
from torch import nn
  

def handler(event, context):
    startTime = time.time()
    model= torch.load('./model/resnet34.pt')
    time_load = time.time() - startTime
    # model.load_state_dict(torch.load('/home/app/function/model/resnet50.pkl'))
    # model= torch.load('./model/resnet34.pt')
    
    x=torch.randn(16,3,224,224)
    output = model(x)
    torch.nn.functional.softmax(output[0], dim=0)
    # print(output)
        
    invoke_time = event['data']['invoke_time']  
    result = {"token": "stream", "invoke_time":invoke_time,"startTime": startTime,"time_load": time_load,"endTime": time.time(), "runtime": time.time()-startTime, "ip":socket.gethostbyname(socket.gethostname())}
    print(result,invoke_time)
    return result

# handler(None)