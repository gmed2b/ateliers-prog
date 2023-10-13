import numpy as np

data = np.loadtxt('sakado.txt')
rapport = data[:, 0] / data[:, 1]
data = np.c_[data, rapport]

