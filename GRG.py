import networkx as nx
from scipy import stats
import numpy as np
import itertools
import matplotlib.pyplot as plt


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

if __name__ == '__main__':
    vertex_distr = stats.norm.rvs(size=100)
    graph = GRG(vertex_distr)
    graph.draw()