docker build . -f perceptron-general.Dockerfile -t  k.harbor.siat.ac.cn/kubeless/perceptron-general:1.2 &&\
docker push  k.harbor.siat.ac.cn/kubeless/perceptron-general:1.2  &&\
kubeless function deploy --runtime-image k.harbor.siat.ac.cn/kubeless/perceptron-general:1.2  --from-file ./handler.py --handler handler.handler --runtime python3.7 perceptron-general -n kubeless --cpu 1000m