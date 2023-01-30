Create a random network using the Erdos-Renyi method (randomly assign a given number of edges to given nodes)

Info:
This script taked as input a file of nodes in a network and the number of edges to randomly assign to the nodes, then assign those
edges to create a network. The results of this file need to be put into BiBC_degree_calculator.py, where the BiBC and degree for each
of the nodes can be calculated.

Usage:
python bootstrap_network.py <list_of_nodes.txt> <number of edges>

Required (positional) arguments:
1. A text file containing just a list of nodes, all in a single column
2. The number of edges to draw randomly between the nodes in the text file
