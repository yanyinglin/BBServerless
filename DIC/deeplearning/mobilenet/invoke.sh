docker build . -f mobilenet.Dockerfile -t  k.harbor.siat.ac.cn/kubeless/mobilenet:1.0 &&\
docker push  k.harbor.siat.ac.cn/kubeless/mobilenet:1.0  &&\
kubeless function deploy  --runtime-image k.harbor.siat.ac.cn/kubeless/mobilenet:1.0 --from-file ./handler.py --handler handler.handler --runtime python3.8 mobilenet -d requirements.txt -n kubeless --cpu 1000m --timeout 1200