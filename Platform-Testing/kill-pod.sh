for p in $( kubectl get pods -n openfaas |grep gateway-7897f8fc66-dhp2v | tail -n +2 | awk -F ' ' '{print $1}'); do kubectl delete pod -n openfaas $p --grace-period=0 --force;done