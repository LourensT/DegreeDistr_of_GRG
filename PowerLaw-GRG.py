from GRG import GRG
from scipy import stats

import numpy as np

import matplotlib.pyplot as plt


n = 10000
tau = 3.5
a = 1

'''
sample a single weight (according to powerlaw distribution in #6.2.21 form vol1
'''
def sampleWeight(size):

    weights = np.zeros(size)

    for i in range(size):
        w = a*(((i+1)/size)**(-1/(tau -1)))
        weights[i] = w

    return weights

graph = GRG(sampleWeight(n))
distr = graph.DegreeDistribrution()
plt.loglog(distr.keys(), distr.values(), color='blue')
plt.show()