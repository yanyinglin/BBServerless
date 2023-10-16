import time
import json
import torch
import socket
from torch import nn
# from function.ClassAll import CNNnet


class CNNnet(nn.Module):

    def __init__(self):
        super(CNNnet,self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(in_channels=1,
                            out_channels=16,
                            kernel_size=3,
                            stride=2,
                            padding=1),
            nn.BatchNorm2d(16),
            nn.ReLU()
        )
        self.conv2 = nn.Sequential(
            nn.Conv2d(16,32,3,2,1),
            nn.BatchNorm2d(32),
            nn.ReLU()
        )
        self.conv3 = nn.Sequential(
            nn.Conv2d(32,64,3,2,1),
            nn.BatchNorm2d(64),
            nn.ReLU()
        )
        self.conv4 = nn.Sequential(
            nn.Conv2d(64,64,2,2,0),
            nn.BatchNorm2d(64),
            nn.ReLU()
        )
        self.mlp1 = nn.Linear(2*2*64,100)
        self.mlp2 = nn.Linear(100,10)

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.conv3(x)
        x = self.conv4(x)
        x = self.mlp1(x.view(x.size(0),-1))
        x = self.mlp2(x)
        return x


def handle(args):
    from ClassAll import CNNnet
    startTime = time.time()
    
    model = CNNnet()
    model = torch.load('/home/app/function/model/cnn.pkl')
    model= torch.load('./model/cnn.pkl')

    output = model(torch.randn(128,1,28,28))
    m = torch.nn.functional.softmax(output[0], dim=0).detach().numpy().tolist()
    # print(output)
    time_load = time.time() - startTime
    print({"token": "inference finished", "startTime": startTime,"time_load": time_load,"endTime": time.time(), "runtime": time.time()-startTime, "ip":socket.gethostbyname(socket.gethostname())})
    return {"token":  "inference finished", "startTime": startTime,"endTime": time.time(),"runtime": time.time()-startTime,"ip":socket.gethostbyname(socket.gethostname())}


handle(None)
