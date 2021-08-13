# GRG with Powerlaw weights example

inspect the degree distribution of a Generalized Random Graph. Implementation of GRG with Powerlaw distributed weights.

We expect that the tail degree distribution also obeys a powerlaw.

Additionally, calculate the size of the giant component with getSizeOfGiantComponent()
* Note: Strictly speaking, we assume the GRG is highly connected, that is, as n -> \inf, 
    liminf of the ( size of the largest connected component / size of network) > 0.)

Also, calculate the typical distance (distribution of the shortest paths). 