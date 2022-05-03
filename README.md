# Generative Models Syntethic Dataset (GMSD)

![alt text](https://github.com/eyalbetzalel/gmsd/blob/main/gmsd_examples.jpg)

An auxiliary dataset, Generative Models Synthetic Dataset (GMSD), of 100K images created by using ImageGPT model that has been trained on ImageNet32. GMSD was created by generating samples from a complex probability density function (1M epochs on ImageGPT), and since ImageGPT is an AR model, the explicit likelihood for each sample can be measured. GMSD is split to training set (70K images), validation set (20K images) and test set (10k images).

## Depencdnices

pip install torch

## Run

python get_gmsd.py

## References

Soon...
