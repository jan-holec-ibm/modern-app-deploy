
## Podman init
```bash 
podman machine init --cpus=4 --memory=4096 -v $HOME:$HOME -v /private/tmp:/private/tmp -v /var/folders/:/var/folders/

sudo /opt/homebrew/Cellar/podman/4.6.0/bin/podman-mac-helper install
podman machine stop; podman machine start

podman machine list
```

## Run app localy

```bash
python3 app.py
HELLO_STR=Jan python3 app.py
```

## Build container image

```bash
podman build -t hello .

podman build -t hello --build-arg MAINTAINER="Jan Holec" --build-arg HELLO_STR="Jan" .
```

## Inspect images and containers

```bash 
podman inspect localhost/hello:latest | jq -r '.[].Labels, .[].Config'
podman inspect localhost/hello:latest | jq -r '.[] | .Config.Env'
podman inspect localhost/hello:latest | jq -r '.[] | .Config.Env[] | select(. | test("^HELLO_STRING.*"))'
```

## Run containers

```bash
podman run --rm --name hello-container hello
podman run --rm --name hello-container -p 5000:5000 hello

run -d -e HELLO_STR="Inline var" --name hello-container -p 5000:5000 hello

podman top hello-container
podman stats hello-container

podman search nginx

podman run -d --name hello-container -p 5000:5000 hello
podman exec -ti hello-container bash

apt update && apt install -y vim

podman stop hello-container
podman start hello-container

podman rm -f hello-container

podman run -d --name hello-container -p 5000:5000 -v hello-persistent:/python-docker hello
podman exec -ti hello-container bash

podman run --rm --name hello-container \
  -p 5000:5000 \
  -v $(pwd)/app.py:/python-docker/app.py \
  hello
```

## Save and export images from archive

```bash
podman save -o hello_image.tar hello:latest
podman load -i hello_image.tar
```

## Podman-compose

```bash
podman-compose up
podman-compose up -d
podman-compose up -d --force-recreate
podman-compose stop
podman-compose start
podman-compose down
```

## Working with image registry

```bash
podman login -u="jan_holec_ibm+cvut_demo" \
  -p="X3RN66EE9AWVCS3KSUIAV5DXGWDB57ZUQX0JQASB29B2UU1S46MR9N0U27132QK7" \
  quay.io
```

```bash 
podman build -t quay.io/jan_holec_ibm/cvut_containers:holecj --platform=linux/amd64 .
podman tag hello quay.io/jan_holec_ibm/cvut_containers:holecj

podman push quay.io/jan_holec_ibm/cvut_containers:holecj
```

## Kubecl 

https://kubernetes.io/docs/reference/kubectl/cheatsheet/

```bash

kubectl get <resource>

kubectl apply -f <resource>

kubectl logs <pod> -c <container>

kubectl exec <pod> -c <container> -- <command>

```


```bash
kubectl create secret docker-registry regcred --docker-server=<your-registry-server> --docker-username=<your-name> --docker-password=<your-pword> --docker-email=<your-email>
```