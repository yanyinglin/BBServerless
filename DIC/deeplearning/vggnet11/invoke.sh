docker build . -f vggnet11.Dockerfile -t  k.harbor.siat.ac.cn/kubeless/vggnet11:1.0.1 &&\
docker push  k.harbor.siat.ac.cn/kubeless/vggnet11:1.0.1  &&\
kubeless function deploy  --runtime-image k.harbor.siat.ac.cn/kubeless/vggnet11:1.0.1 --from-file ./handler.py --handler handler.handler --runtime python3.8 vggnet11 -d requirements.txt -n kubeless --cpu 1000m --timeout 1200