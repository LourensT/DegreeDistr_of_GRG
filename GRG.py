import networkx as nx
from scipy import stats
import numpy as np
import itertools
import matplotlib.pyplot as plt

import tikzplotlib as plt2tikz

from DegreeDistributions.DegreeDistributions import *

class GRG:

    '''

    @param n: number of vertices
    @param weigh_weights: array or list of the weights of all vertices, length determines sizes of GRG

    '''
    def __init__(self, vertex_weights):
        self.vertex_weights = {}
        self.weights_sum = sum(vertex_weights)
        self.n = len(vertex_weights)

        # add vertices
        self.G = nx.Graph()
        for i, weight in enumerate(vertex_weights):
            self.G.add_node(i)
            self.vertex_weights[i] = weight

        # vertices
        benches = self._sampleUniformForSimulation((self.n*(self.n-1)/2))
        for (v1, v2) in itertools.combinations(self.vertex_weights.keys(), r=2):
            if self.weightProbability(v1, v2) >= benches.pop():
                self.G.add_edge(v1, v2)

    def draw(self):
        nx.draw(self.G)
        plt.show()

    def weightProbability(self, v1, v2):
        w1 = self.vertex_weights[v1]
        w2 = self.vertex_weights[v2]
        return (w1*w2 / ((w1*w2) + self.weights_sum))

    def _sampleUniformForSimulation(self, len):
        return list(stats.uniform.rvs(size=int(len)))

    def DegreeDistribrution(self):
        return DegreeDistribution(self.G, tail=True)

    def RandomFriendDegreeDistribution(self):
        return RandomFriendDegreeDistribution(self.G, tail=True)

    def SizeBiasedDegreeDistribution(self):
        return SizeBiasedDegreeDistribution(self.G, tail=True)

    '''
    Returns size of largest connected component (giant components)

    Note: Strictly speaking, we assume the GRG is highly connected, that is, as n -> \inf, 
    liminf of the ( size of the largest connected component / size of network) > 0.
    '''
    def getSizeOfGiantComponent(self):
        # get sorted list of size of all connected components
        component_sizes = [len(c) for c in sorted(nx.connected_components(self.G), key=len, reverse=True)]
        return component_sizes[0]

    '''
    Returns distribution of typical distance:

    the length of the shortest path between two randomly drawn nodes, given that they are connected
    '''
    def typicalDistanceDistribution(self):
        #dictionary of dictionaries
        all_shortest_paths = nx.algorithms.shortest_path(self.G)

        pmf = {}
        numberOfPaths = 0
        for source, destinations in all_shortest_paths.items():
            for destination, path in destinations.items():
                if len(path) in pmf:
                    pmf[len(path)] += 1
                else: 
                    pmf[len(path)] = 1
                numberOfPaths += 1
        
        #normalize the histogram (paths currently double counted)
        for key in pmf.keys():
            pmf[key] = pmf[key] / numberOfPaths

        assert abs(sum([v for v in pmf.values()]) - 1) < 0.00001, "pmf does not sum to one!!"

        return pmf

if __name__ == '__main__':
    vertex_distr = stats.norm.rvs(size=100)
    graph = GRG(vertex_distr)
    graph.draw()
    #graph.saveDegreeDistribution('plot.tikz', show=True)