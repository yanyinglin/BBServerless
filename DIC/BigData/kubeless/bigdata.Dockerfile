# Create a custom image with a python function
FROM k.harbor.siat.ac.cn/kubeless/pyton-datadog-38:v1.0
ENV FUNC_HANDLER=handler MOD_NAME=handler
ADD handler.py /kubeless/
WORKDIR /kubeless/
ENTRYPOINT [ "python" ,"/_kubeless.py"]