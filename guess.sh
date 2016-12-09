#!/bin/bash
SCRIPT=`realpath $0`
SCRIPTPATH=`dirname $SCRIPT`
nvidia-docker run \
        -v $SCRIPTPATH:/mnt \
	tensorflow/tensorflow:0.10.0-devel "/mnt/src/guess.sh"

