#!/bin/bash

#SBATCH --gpus=1
#SBATCH --time=04:00:00
#SBATCH --cpus-per-gpu=4
#SBATCH --job-name=LinClassTinyImagenet
#SBATCH --output=out-LinClass-TinyImagenet-%J.out

module load anaconda/anaconda3
module load cuda/cuda-10.0

source activate /home/cap6614.student6/my-envs/feat-decoupling

echo
time python /home/cap6614.student6/feature-decoupling/pytorch_feature_decoupling/main.py --exp=ImageNet_LinearClassifiers_ImageNet_Decoupling_AlexNet_Features --evaluate 0 --num_workers 4
echo

# You're done!
echo "Ending script..."
date