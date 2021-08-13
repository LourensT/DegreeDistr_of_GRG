from GRG import GRG
from scipy import stats

import numpy as np

import matplotlib.pyplot as plt


n = 1000
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


weights = sampleWeight(n)
graph = GRG(weights)

# calculate tail distribution of weights
weights.sort()
total = sum(weights)
cumulative = [sum(weights[n::])/total for n in range(len(weights))]
prev = weights[0]
index = [prev]
freq = [cumulative[0]]
for i in range(1, len(weights)):
    if not (weights[i] == prev):
        prev = weights[i]
        index.append(weights[i])
        freq.append(cumulative[i])

# plot weight distribution
plt.scatter(x=index, y=freq, color='blue')
plt.title("Tail Distribution of vertex weights, tau=3.5, alpha=1")
plt.show()


distr = graph.DegreeDistribrution()
distrBiased = graph.SizeBiasedDegreeDistribution()
# plot degree distribution
plt.scatter(x=distr.keys(), y=distr.values(), color='red')
plt.scatter(x=distrBiased.keys(), y=distrBiased.values(), color='green')
plt.legend(["Normal Degree Distribution", "size Biased Degree Distribution"])
plt.title("Tail Distributions of degrees, tau=3.5, alpha=1")
plt.show()

print("Size of Giant Component", graph.getSizeOfGiantComponent())