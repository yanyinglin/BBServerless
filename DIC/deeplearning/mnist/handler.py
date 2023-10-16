import time
import json
import torch
from torch import nn
import socket

class MnistModel(nn.Module):
    def __init__(self):
        super(MnistModel, self).__init__()#父类初始化命令行
        self.fc1 = nn.Linear(1*128*128, 100)  # 28是像素，最终为什么是 10，因为手写数字识别最终是10(0,1,2,3,4,5,6,7,8,9)分类的，分类任务中有多少，就分几类
        self.relu = nn.ReLU()#激活函数
        self.fc2 = nn.Linear(100, 10)#线性层
 
    def forward(self, image):
        image_viwed = image.view(-1, 1*128*128)  #重点： 此处需要拍平
        out_1 = self.fc1(image_viwed)
        fc1 = self.relu(out_1)#激活函数
        out_2 = self.fc2(fc1)
        return out_2
 
 
 
def handler(event, context):
    startTime = time.time()
    model = MnistModel()
    model.load_state_dict(torch.load("./model/minist.pkl"))
    time_load = time.time() - startTime
    
    result = model(torch.randn(100, 2, 128, 128)).detach().numpy().tolist()
    
    invoke_time = event['data']['invoke_time']
    result = {"token": "stream", "invoke_time":invoke_time,"startTime": startTime,"time_load": time_load,"endTime": time.time(), "runtime": time.time()-startTime, "ip":socket.gethostbyname(socket.gethostname())}
    print(result,invoke_time)
    return result

# handler(None)
