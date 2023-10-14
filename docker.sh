#!/bin/bash
#docker login --username=pevans927
# including --platform linux/amd64 is necessary to build on M1 Macs
#docker buildx build --load --platform linux/amd64 -t pevans927/umarket:latest .
#docker push pevans927/umarket:latest
doctl auth init -context umarket
doctl registry login -context umarket
docker buildx build --load --platform linux/amd64 -t registry.digitalocean.com/umarket/umarket:latest .
docker push registry.digitalocean.com/umarket/umarket:latest