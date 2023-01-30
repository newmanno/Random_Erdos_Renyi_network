# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 00:57:38 2021

@author: Nolan Newman <newmanno@oregonstate.edu>    
"""

import csv
import sys
import numpy as np
import networkx as nx
import pickle
from math import factorial

# Import node list file from user and get number of desired edges for bootstrapped network
input_file = sys.argv[1] # .txt file containing just the list of nodes in the network
num_edges = int(sys.argv[2]) # just a single integer of the number of edges

edge_list = []

# Function that calculates the number of possible edges in the network
def num_possible_edge(num_nodes, input_edges):
    num_possible = int(factorial(num_nodes)/(2 * factorial(num_nodes - 2)))
                           
    if int(input_edges) <= int(num_possible):
        return True
    else:
        return False
                       
# Function that will randomly assign edges to pairs of nodes; function called by make_net 
def rand_nodes(net):
    i = 0
    while i < 1:
    
        # Randomly choose two nodes to create an edge between
        two_nodes = np.random.choice(G.nodes, 2, replace = False)

        # Check if this edge already exists in the network. If it does, then 
        # do not add it to the network and instead choose 2 different nodes
        if net.has_edge(two_nodes[0], two_nodes[1]):
            i = 0
        else:
            i = 1

    # returns an ndarray (pretty much a list) of the two randomly chosen nodes
    return(two_nodes)

# Function that will request an edge gets added for every edge the user requests. Calls rand_nodes.
def make_net(G, n_edge): 
    # loop through as many times as needed (as determined by the user's num_edges input
    for i in range(1, (n_edge + 1)):    # Need to add 1 b/c last number is exclusive
        random_edge = rand_nodes(G)    # Pass network to rand_nodes to pick two random nodes
        G.add_edge(random_edge[0],random_edge[1])    # add edge between those two random nodes
    return(G)

node_list = []

if __name__ == '__main__':

    ###########################################################################
    ###    First, import a list of nodes and the number of edges        ###
    ###########################################################################

    # Find all nodes from input file, reading through the file one line at a time
    # and adding each node (per line) to a node list
    node_file = open(input_file, 'r')
    for line in node_file:
        node_list.append(line[:-1]) #[:-1] is to remove the newline char 
    
    unique_nodes = np.unique(node_list)

    print(node_list)

    print("The network being bootstrapped has " + str(num_edges) + " edges and " + str(len(unique_nodes)) + " nodes")

    pass_check = False
    
    while pass_check == False:

        pass_check = num_possible_edge(len(unique_nodes), num_edges)
    
        if pass_check == False:
            print("#####ERROR!#####\nThe number of desired edges must be smaller than the following:\n        number of total nodes      \n    ------------------------------\n    2(number of total nodes - 2)!)")
            num_edges = int(input("How many edges do you want to simulate in this random network?"))
            #0/0 # Force a crash of the program
        else:
            pass
                    

    ###################################################################################
    ###    Second, generate a network that has edges randomly assigned to nodes    ###
    ###################################################################################
    G = nx.Graph()

    # Add all the nodes to the graph
    G.add_nodes_from(unique_nodes)
    
    # Pass the graph to the make_net function, which will assign the random edges to pairs of nodes, ensuring
    # no pairs get an edge twice (i.e. ensuring the total number of edges is the one the user requests)
    G = make_net(G, num_edges)

    print("Finished making network with " + str(len(G.edges())) + " edges and " + str(len(G.nodes())) + " nodes.")

    pickle_out = open("bootstrap.pickle", "wb")
    pickle.dump(G, pickle_out)
    pickle_out.close()

print("Done saving pickle!")





