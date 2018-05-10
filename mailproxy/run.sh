#!/bin/bash

docker run -p 9011:9011 --name mailproxy -v `{pwd}`/mailproxy:/etc/mailproxy -d mailproxy:latest
