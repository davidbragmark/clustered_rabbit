#!/bin/sh

docker stop rabbitmq-node-1
docker stop rabbitmq-node-2
docker stop rabbitmq-node-3
docker rm rabbitmq-node-1
docker rm rabbitmq-node-2
docker rm rabbitmq-node-3
docker stop haproxy
docker rm haproxy
