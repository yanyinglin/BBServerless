# Create a custom image with a python function
FROM k.harbor.siat.ac.cn/kubeless/pythonml:3.8.1
# tag: k.harbor.siat.ac.cn/kubeless/stream:1.0
# build:  docker build . -t k.harbor.siat.ac.cn/kubeless/stream:1.0 -f stream.Dockerfile

ENV FUNC_HANDLER=handler MOD_NAME=handler
ADD handler.py /kubeless/
ADD model/svr-general /kubeless/model/
ADD data/svr-general /kubeless/data/
WORKDIR /kubeless/
ENTRYPOINT [ "python" ,"/_kubeless.py"]