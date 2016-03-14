#!/usr/bin/env sh

./build/tools/caffe train \
    --solver=models/spl2016/cough_alexnet/solver.prototxt
