docker build . -f cryptography.Dockerfile -t  k.harbor.siat.ac.cn/kubeless/cryptography-cloud:1.0 &&\
docker push  k.harbor.siat.ac.cn/kubeless/cryptography-cloud:1.0  &&\

kubeless function deploy --runtime-image k.harbor.siat.ac.cn/kubeless/cryptography:1.0 --from-file ./handler.py --handler handler.handler -r python3.8 cryptography -d requirements.txt -n kubeless --cpu 500m --timeout 500