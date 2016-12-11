#!/bin/bash

cd /tensorflow && \
python tensorflow/examples/image_retraining/retrain.py \
	--bottleneck_dir=/mnt/model/bottlenecks \
	--how_many_training_steps 500 \
	--model_dir=/mnt/model/inception \
	--output_graph=/mnt/model/retrained_graph.pb \
	--output_labels=/mnt/model/retrained_labels.txt \
	--image_dir=/mnt/train_images
