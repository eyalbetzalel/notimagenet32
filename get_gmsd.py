import torch
import os

os.system('wget https://www.dropbox.com/s/hnojjtkeql9z2n3/gmsd.tar.gz')
os.system('tar -xvzf gmsd.tar.gz')
X_train, y_train = torch.load('./gmsd/gmsd_train.pt')
X_test, y_test = torch.load('./gmsd/gmsd_test.pt')
