docker build . -f resnet34.Dockerfile -t  k.harbor.siat.ac.cn/kubeless/resnet34:1.0 &&\
docker push  k.harbor.siat.ac.cn/kubeless/resnet34:1.0  &&\
kubeless function deploy  --runtime-image k.harbor.siat.ac.cn/kubeless/resnet34:1.0 --from-file ./handler.py --handler handler.handler --runtime python3.8 resnet34 -d requirements.txt -n kubeless --cpu 1000m  --timeout 1200