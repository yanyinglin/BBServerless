docker build . -f multinomialnb-general.Dockerfile -t  k.harbor.siat.ac.cn/kubeless/multinomialnb-general:1.2 &&\
docker push  k.harbor.siat.ac.cn/kubeless/multinomialnb-general:1.2  &&\
kubeless function deploy --runtime-image k.harbor.siat.ac.cn/kubeless/multinomialnb-general:1.2  --from-file ./handler.py --handler handler.handler --runtime python3.7 multinomialnb-general -n kubeless --cpu 1000m