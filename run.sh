#!/bin/bash


# Also docker build -t facerecdb .
docker run -it -p 5000:5000 -v /db:/db facerecdb
