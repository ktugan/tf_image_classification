#!/bin/bash

nvidia-docker run --rm -it \
	-v `pwd`:/mnt tensorflow/tensorflow:0.10.0-devel-gpu \
	"/mnt/src/train.sh"