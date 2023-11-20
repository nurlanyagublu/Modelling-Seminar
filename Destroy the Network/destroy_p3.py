#Nurlan Yagublu 
#G72RIJ

import numpy as np
import networkx as nx
import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument('-g', '--graph', dest='graph', action='store', default=None)
args = parser.parse_args()

if not args.graph:
    print("Need a graph as input")
    exit()

def read_graph(graph_file):
    with open(graph_file) as f:
        n = int(f.readline())
        m = int(f.readline())
        A = [[0] * n for _ in range(n)]
        for _ in range(m):
            [u, v] = map(int, f.readline().split())
            A[u][v] = 1
            A[v][u] = 1
    G = nx.Graph(np.array(A))
    return G

def max_comp_size(G):
    return max([len(c) for c in nx.connected_components(G)])

G = read_graph(args.graph)
n = len(G.nodes)


nodes_by_degree = sorted(G.nodes, key=lambda x: -len(list(G.neighbors(x))))


remaining_nodes = set(G.nodes)
removed_nodes = []

# Continue removing nodes until the largest connected component size is less than 500
while max_comp_size(G) > 500 and len(nodes_by_degree) > 0:
    node_to_remove = nodes_by_degree.pop(0)
    if node_to_remove in remaining_nodes:
        remaining_nodes.remove(node_to_remove)
        removed_nodes.append(node_to_remove)
        G.remove_node(node_to_remove)


for u in removed_nodes:
    print(u)