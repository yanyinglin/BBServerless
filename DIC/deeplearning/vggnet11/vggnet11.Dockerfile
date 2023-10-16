# Create a custom image with a python function
FROM k.harbor.siat.ac.cn/kubeless/pythonml:3.8.1
# tag k.harbor.siat.ac.cn/kubeless/vggnet11:1.0.1  
ENV FUNC_HANDLER=handler MOD_NAME=handler
ADD handler.py /kubeless/
ADD model/vggnet11.pt /kubeless/model/
WORKDIR /kubeless/
# ADD data/facerecognition-general /kubeless/data/
ENTRYPOINT [ "python" ,"/_kubeless.py"]
