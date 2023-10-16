docker build . -f resnet50.Dockerfile -t  k.harbor.siat.ac.cn/kubeless/resnet50:1.0 &&\
docker push  k.harbor.siat.ac.cn/kubeless/resnet50:1.0  &&\
kubeless function deploy  --runtime-image k.harbor.siat.ac.cn/kubeless/resnet50:1.0 --from-file ./handler.py --handler handler.handler --runtime python3.8 resnet50 -d requirements.txt -n kubeless --cpu 1000m --timeout 1200