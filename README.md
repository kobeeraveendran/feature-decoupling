# *Feature Decoupling++*

## Note

* Experiment-related data will be stored in the directories [_experiments](https://github.com/kobeeraveendran/feature-decoupling/tree/master/_experiments) and [_experiments_conversion](https://github.com/kobeeraveendran/feature-decoupling/tree/master/_experiments_conversion).

* In `config_env.py`, change the `IMAGENET_DIR` path variable to the path of the Tiny ImageNet dataset's root folder (`tiny-imagenet-200`).

## Environment Setup

I have provided the `conda` environments that I used for training, evaluation, and visualization.

### Newton

If running the code on Newton, chances are you may re-create my full environment in `environment_verbose.yml`. However, you will have to change the `name` value in this file to the full path that it would have on Newton, such as `/home/<newton_username>/my-envs/feat-decoupling`. You may then create the environment like so:

```bash
conda create -f environment_verbose.yml
```

### Cross-platform

If you ran into issues creating the verbose environment, you can use the more generic version (`environment_concise.yml`). If trying this on Newton, again make sure to change the name of the environment to the full path in `my-envs`. Otherwise, leave it as is.

Create this environment by running:

```bash
conda create -f environment_concise.yml
```

### Manual

If none of the above automatic methods worked, you may also install the packages manually depending on your system and CUDA configurations (it is recommended to install CUDA v10.0 with cuDNN7).

```bash
conda create -n feat-decoupling python=3.6.5 -y
conda activate feat-decoupling
conda install pytorch==1.0.1 torchvision==0.2.2 cudatoolkit=10.0 -c pytorch -y
conda install -c conda-forge tqdm -y
pip install torchnet
```

Exact versions I used for any of the dependencies can be found in [`environment_verbose.yml`](https://github.com/kobeeraveendran/feature-decoupling/blob/master/environment_verbose.yml).

## Running Experiments

To train a FeatureDecoupling++ model on Tiny ImageNet, see the instructions in [pytorch_feature_decoupling](https://github.com/kobeeraveendran/feature-decoupling/tree/master/pytorch_feature_decoupling). I have included some of the FeatureDecoupling authors' instructions as well, in the event that you are not running this on Newton.
