docker build . -f svr-general.Dockerfile -t  k.harbor.siat.ac.cn/kubeless/svr-general:1.2 &&\
docker push  k.harbor.siat.ac.cn/kubeless/svr-general:1.2  &&\
kubeless function deploy --runtime-image k.harbor.siat.ac.cn/kubeless/svr-general:1.2  --from-file ./handler.py --handler handler.handler --runtime python3.7 svr-general -n kubeless --cpu 1000m