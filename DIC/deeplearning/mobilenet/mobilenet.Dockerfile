# Create a custom image with a python function
FROM k.harbor.siat.ac.cn/kubeless/pythonml:3.8.1
# tag k.harbor.siat.ac.cn/kubeless/mobilenet:1.0  
ENV FUNC_HANDLER=handler MOD_NAME=handler
ADD handler.py /kubeless/
ADD model/mobilenet_v11_3.pt /kubeless/model/
# ADD data/facerecognition-general /kubeless/data/
WORKDIR /kubeless/
ENTRYPOINT [ "python" ,"/_kubeless.py"]
