Create a random network using the Erdos-Renyi method (randomly assign a given number of edges to given nodes)

Info:
This script taked as input a file of nodes in a network and the number of edges to randomly assign to the nodes, then assign those
edges to create a network. The results of this file need to be put into BiBC_degree_calculator.py, where the BiBC and degree for each
of the nodes can be calculated.

Usage:
python bootstrap_network.py <list_of_nodes.txt> <number of edges>

Example input file:
node1
node2
node3
<blank line>

***NOTE: The blank line at the end of the file is crucial or else it will strip the last character from the last node in the node list.
    
