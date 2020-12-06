# *Feature Decoupling++*

## Setup

* Experiment-related data will be stored in the directories [_experiments](https://github.com/kobeeraveendran/feature-decoupling/tree/master/_experiments) and [_experiments_conversion](https://github.com/kobeeraveendran/feature-decoupling/tree/master/_experiments_conversion).

* In *config_env.py*, change the `IMAGENET_DIR` path to the path to Tiny ImageNet dataset's root folder (`tiny-imagenet-200`).

## Experiments

* In order to train a Feature Decoupling++ model in an unsupervised way with AlexNet-like architecture on the ImageNet training images and then evaluate linear classifiers as well as non-linear classifiers (for Tiny ImageNet) on top of the learned features please visit the [pytorch_feature_decoupling](https://github.com/kobeeraveendran/feature-decoupling/tree/master/pytorch_feature_decoupling) folder.
