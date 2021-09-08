from GRG import GRG
from TikzPlotsFromPython.GenerateTikz import GenerateTikz
import os

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

BASE_FP = os.getcwd() + "\\Plots\\"
print(BASE_FP)

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



# get degree distributions
distr = graph.DegreeDistribrution(tail=True)
distrSizeBiased = graph.SizeBiasedDegreeDistribution(tail=True)
distrfriendBiased = graph.RandomFriendDegreeDistribution(tail=True)

# tikz object
plot = GenerateTikz(os.path.join(BASE_FP, "degree_distribution.tikz"), documentation=f"Degree distributions of GRG (n={n}) with Powerlaw (tau=={tau}) distributed weights, following #6.2.21 from Hofstad RGCN Vol1. ")
maximum_degrees = max(max(max(distr.keys()), max(distrSizeBiased.keys())), max(distrfriendBiased.keys()))
plot.setConfiguration(0, maximum_degrees, 0, 1, False, False, xlabel="Degrees", ylabel="$P(X > x)$")

# plot degree distribution
plt.scatter(x=distr.keys(), y=distr.values(), color='red')
plot.addSeries(distr, "Degree distribution")
plt.scatter(x=distrSizeBiased.keys(), y=distrSizeBiased.values(), color='green')
plot.addSeries(distrSizeBiased, "Size biased degree distribution")
plt.scatter(x=distrfriendBiased.keys(), y=distrfriendBiased.values(), color='blue')
plot.addSeries(distrfriendBiased, "Random friend degree distribution")
plt.legend(["Normal Degree Distribution", "size Biased Degree Distribution", "Random friend degree distribution"])
plt.title("Tail Distributions of degrees, tau=3.5, alpha=1")
plt.show()

print("Size of Giant Component", graph.getSizeOfGiantComponent())

typicalDist = graph.typicalDistanceDistribution()

plot_distance = GenerateTikz(os.path.join(BASE_FP, "typical_distance.tikz"), documentation=f"Distribution of typical distance of GRG (n={n}) with Powerlaw (tau=={tau}) distributed weights, following #6.2.21 from Hofstad RGCN Vol1.")
plot_distance.setConfiguration(0, max(typicalDist.keys()), 0, max(typicalDist.values()), False, False, xlabel="Typical Distance")
# plot distance distribution
plt.scatter(x=typicalDist.keys(), y=typicalDist.values(), color='red')
plot_distance.addSeries(typicalDist, "Typical Distance")
plt.title("Typical distance distribution, tau=3.5, alpha=1")
plt.show()