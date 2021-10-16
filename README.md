# GRG with power law distributed weights example

RGCN = Random Graphs and Complex Networks by Remco van der Hofstad, respectively volume 1 and 2. 

Here we consider the GRG model (Generalized Random Graph), as defined in chapter 6 of RGCN II. The weights are powerlaw distributed as described in equation 6.2.1, for both $\tau = 2.5$ and $\tau = 3.5$.

The objective is to inspect three different definitions for a degree distribution. The conventional definition, the size-biased definition (1.2.2 in RGCN I), and the random friend distribution (the degree distribution of a uniformly selected adjacent vertex to a uniformly selected vertex in the network). See the submodule DegreeDistributions for more details. 

Both networks generated in the preview.pdf are of size $N = 10000.$ For the case with $\tau = 2.5$, the giant component is of size $7797$, for the case with $\tau = 3.5$, the giant component is $6476$. 

The `GRG` class defined in `GRG.py` support generic weights, the `Powerlaw-GRG.py` gives an example where the weights are powerlaw distributed.