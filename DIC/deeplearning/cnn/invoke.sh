
docker build . -f lstm.Dockerfile -t  k.harbor.siat.ac.cn/kubeless/cnn:1.0 &&\
docker push  k.harbor.siat.ac.cn/kubeless/cnn:1.0  &&\
kubeless function deploy  --runtime-image k.harbor.siat.ac.cn/kubeless/cnn:1.0 --from-file ./handler.py --handler handler.handler --runtime python3.8 cnn -d requirements.txt -n kubeless --cpu 1000m
