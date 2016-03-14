#!/usr/bin/env sh
# Compute the mean image from the imagenet training lmdb
# N.B. this is available in data/ilsvrc12

EXAMPLE=examples/cough_2016
DATA=data/cough_data
TOOLS=build/tools

$TOOLS/compute_image_mean $EXAMPLE/cough_train_lmdb \
  $DATA/cough_mean.binaryproto

echo "Done."
