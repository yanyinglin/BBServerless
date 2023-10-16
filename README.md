# BBServerless

> BBServerless is a benchmark for serverless platforms. It is designed to evaluate the performance of serverless platforms in the context of machine learning, webservice, streaming processing and deep learning inference.

## Installation & Cluster Configuration

How to use this benchmark to evaluate the performance of serverless platforms? We provide a detailed description of the installation and configuration of the benchmark and the serverless platforms.

We provide a detailed description of the installation and configuration of serverless platforms: openwhisk, openfaas, kubeless.




### how to use BBServerless
1. installed kubernetes cluster, with 3 or more server.
2. docker, helm3 installed; if you using local repository, you need to install harbor, and login into it by `docker login`.
3. download the deep learning model file and bigdata train.txt (you can generat this train.txt using any content, like a novel) using script `download_model.ipynb` in `DIC/envs/download_model.ipynb`, or you can just replace it using your own model file.
4. install prometheus and grafana, and config the prometheus datasource in grafana, and install loki to collect print log of function if you need to collect more detail informations.



## Steps for starting the benchmark
> These steps are for reference only, please refer to the detailed description for specific operations.

### Serverless Platfroms installation

- `install Openwhisk` using our helm chart configs, we change the default concurrency limit settings.

```bash
  cd platform-install/openwhisk/helm/openwhisk && helm install openwhisk -n openwhisk --create-namespace .
  cd ../../ && cp wsk /usr/local/bin/
```

- config openwhisk cli

```bash
  wsk property set --apihost serverless.siat.ac.cn:31001
  wsk property set --auth 23bc46b1-71f6-4ed5-8c54-816aa4f8c502:123zO3xZCLrMN6v2BKK1dXYFpXlPkccOFqm12CdAsMgRU4VrNZ9lyGVCGuMDGIwP
```

- `install openfaas` using helm chart. We save the official helm chart in `platform-install/openfaas/helm/faas-netes` to avoid the network problem.

```bash
  cd ../openfaas/faas-netes/ && ./install.sh
```

- config openfaas client faas-cli and set the gateway url, you can set it to ~/.bashrc. We disable the basic_auth of openfaas, so it dont need to set the password.
```bash   
  export OPENFAAS_URL=http://serverless.siat.ac.cn:31112

  # test openfass 
  faas-cli list

  cd bbserverlees/DIC/WebServices/openfaas/python-code/openfaas.yml && faas-cli up -f openfaas.yml

  curl -s http://serverless.siat.ac.cn:31112/function/hello.openfaas-fn
```





- `install kubeless` using yaml file.
```bash
  cd ../../kubeless/
  cp bundles/kubeless /usr/local/bin/
  kubectl create namespace kubeless
  kubectl version

  #If you are using a version of Kubernetes before v1.16, please use the v1beta1 file;
  kubectl create -f ./kubeless-v1.0.8-v1beta1.yaml
  # otherwise, please use the v1 file
  kubectl create -f ./kubeless-v1.0.8-v1.yaml
```

### Machine Learning

```bash
  # create ml env, and generate ml models.
  mkdir -p DIC/envs/Runtimes/ml-inference-with-data-RT/models
  mkdir -p DIC/envs/Runtimes/ml-inference-with-data-RT/testData
  cd DIC/envs/ML_model_training
  pip install -r requirements.txt
  python3 -m pip install --upgrade Pillow
  python3 Classification.py
  python3 FaceRecognition.py
  python3 Linear_Regression.py
```

- create ml code

```bash
  cd ../../MachineLearning/code-creating
  python3  kubeless-func-generate-ml.py
  python3  openfaas-function-generate-ml.py
  python3  openwhisk-function-generate-ml.py
```

## Deploy and push functions

- kubeless auto deploy function by python script.

```bash
  cd ../../envs
  python3 deploy_kubeless.py
```

- openwhisk

```bash
  cd DIC/envs/

  python3 deploy_openwhisk.py
```

- openfaas

```bash
  # install hey
  wget https://hey-release.s3.us-east-2.amazonaws.com/hey_linux_amd64
  chmod +x hey_linux_amd64
  mv hey_linux_amd64 /usr/local/bin/hey

  cd DIC/MachineLearning/Inference-of-ml-openfaas
  python3 deploy_openfaas.py

  #deploy_openfaas.py
  faas-cli build -f openfass-py-ml-config.yml

  # could use docker push to push image to docker hub, modify the image name in openfass-py-ml-config.yml
  faas-cli push -f openfass-py-ml-config.yml
  faas-cli deploy -f openfass-py-ml-config.yml

  # setting autoscaling
  kubectl autoscale deployment {function} -n openfaas-fn --cpu-percent=85  --min=1  --max=30
  kubectl get hpa/{function} -n openfaas-fn

  # edit hpa config (optional)
  kubectl edit hpa {hpa_name} -n openfaas-fn
```

### Citation
~~~
@inproceedings{li2021bbserverless,
title={Bbserverless: A bursty traffic benchmark for serverless},
author={Lin, Yanying and Ye, Kejiang and Li, Yongkang and Lin, Peng and Tang, Yingfei and Xu, Chengzhong},
booktitle={International Conference on Cloud Computing},
pages={45--60},
year={2021},
organization={Springer}
}
~~~