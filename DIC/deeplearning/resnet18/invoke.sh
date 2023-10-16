docker build . -f resnet18.Dockerfile -t  k.harbor.siat.ac.cn/kubeless/resnet18:1.0 &&\
docker push  k.harbor.siat.ac.cn/kubeless/resnet18:1.0  &&\
kubeless function delete resnet18 -n kubeless;
kubeless function deploy  --runtime-image k.harbor.siat.ac.cn/kubeless/resnet18:1.0 --from-file ./handler.py --handler handler.handler --runtime python3.8 resnet18 -d requirements.txt -n kubeless --cpu 1000m --timeout 1200