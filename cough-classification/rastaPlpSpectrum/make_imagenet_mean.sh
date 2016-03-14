#!/usr/bin/env sh
# Compute the mean image from the imagenet training lmdb
# N.B. this is available in data/ilsvrc12

EXAMPLE=examples/rastaPlpSpectrum
DATA=data/rastaPlpSpectrum
TOOLS=build/tools

$TOOLS/compute_image_mean $EXAMPLE/rastaPlpSpectrum_train_lmdb \
  $DATA/imagenet_mean.binaryproto

echo "Done."
