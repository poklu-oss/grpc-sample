#!/usr/bin/env bash
python -m grpc_tools.protoc --proto_path=. ./micro.proto --python_out=gen --grpc_python_out=gen
export PATH=$PATH:~/go/bin
export GO111MODULE=on
protoc -I=. --go_out=plugins=grpc:gogen/micro micro.proto

