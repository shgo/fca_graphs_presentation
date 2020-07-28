#!/usr/bin/python3
#-*- encoding: utf-8 -*-

import numpy as np
from scipy.misc import comb
import matplotlib.pyplot as plt

def plota_combs(n_max = 20):
    x = np.arange(1, n_max+1)
    y = [np.sum([comb(N=n, k=k) for k in np.arange(1, n+1)])
            for n in np.arange(1, n_max+1)]
    plt.plot(x, y)
    plt.xlabel('# of attributes')
    plt.ylabel('# of possible combinations')
    plt.title('# of all possible combinations of attributes')
    plt.show()

if __name__ == '__main__':
    plota_combs(n_max=5)
    plota_combs(n_max=10)
    plota_combs(n_max=15)
    plota_combs(n_max=20)
