# This file configures platform, path and datasets
import os

PROCESS_UNIT = "gpu" # or "cpu"

# Path to caffe
CAFFE_DIR = os.path.join("/home", "workspace", "caffe")

# Path to the datasets directory
# IMAGENET_DIR = os.path.join("/groups", "arcc", "shared", "datasets", "ImageNet2012nonpub")
IMAGENET_DIR = os.path.join("/home", "cap6614.student6", "datasets", "tiny-imagenet-200")
PLACES205_DIR = os.path.join("/home", "datasets", "Places205")
PASCAL_VOC_2007_DIR = os.path.join("/home", "datasets", "PASCAL", "VOC2007")
PASCAL_VOC_2012_DIR = os.path.join("/home", "datasets", "PASCAL", "VOC2012")
