# Create a custom image with a python function
FROM k.harbor.siat.ac.cn/kubeless/pythonml:3.8.1
# tag k.harbor.siat.ac.cn/kubeless/shufflenet:1.0  
ENV FUNC_HANDLER=handler MOD_NAME=handler
ADD handler.py /kubeless/
ADD model/shufflenet.pt /kubeless/model/
# ADD data/facerecognition-general /kubeless/data/
WORKDIR /kubeless/
ENTRYPOINT [ "python" ,"/_kubeless.py"]
