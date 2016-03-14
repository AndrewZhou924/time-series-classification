#!/usr/bin/env sh
# Compute the mean image from the imagenet training lmdb
# N.B. this is available in data/ilsvrc12

EXAMPLE=examples/12thPlpSpectrum
DATA=data/12thPlpSpectrum
TOOLS=build/tools

$TOOLS/compute_image_mean $EXAMPLE/12thPlpSpectrum_train_lmdb \
  $DATA/imagenet_mean.binaryproto

echo "Done."
