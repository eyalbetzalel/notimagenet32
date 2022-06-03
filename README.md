# NotImageNet32 Dataset

![alt text](https://github.com/eyalbetzalel/gmsd/blob/main/gmsd_examples.jpg)

An auxiliary dataset, NotImageNet32, of 100K images created by using ImageGPT model that has been trained on ImageNet32. NotImageNet32 was created by generating samples from a complex probability density function (1M epochs on ImageGPT), and since ImageGPT is an AR model, the explicit likelihood for each sample can be measured. GMSD is split to training set (70K images), validation set (20K images) and test set (10k images).

## Depencdnices

```pip install torch```

## Run

```python get_notimagenet32.py```

Integerate it in your likelihood based generative model and measure the results. 

## References

Soon...
