#!/usr/bin/env sh
# Compute the mean image from the imagenet training lmdb
# N.B. this is available in data/ilsvrc12

EXAMPLE=examples/12thPlpCepstrum
DATA=data/12thPlpCepstrum
TOOLS=build/tools

$TOOLS/compute_image_mean $EXAMPLE/12thPlpCepstrum_train_lmdb \
  $DATA/imagenet_mean.binaryproto

echo "Done."
