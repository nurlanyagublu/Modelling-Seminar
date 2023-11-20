# Function to read an integer from input
def read_int():
    return int(input())

# Function to read a list of integers from input
def read_int_list():
    return list(map(int, input().split()))

# Function to calculate the number of connected nodes and links for each node
def calculate_connected_nodes_and_links(graph, numNodes):
    num_nodes_connected = {}
    num_links_connected = {}

    for node in range(numNodes):
        neighbors = graph[node]
        num_nodes_connected[node] = len(neighbors)
        num_links_connected[node] = sum(len(graph[neighbor]) for neighbor in neighbors)

    return num_nodes_connected, num_links_connected

# Input
numNodes = read_int()
virusLocation = read_int()
numLinks = read_int()

# Initialize graph
graph = {i: set() for i in range(numNodes)}

# Build the graph
for _ in range(numLinks):
    i, j = read_int_list()
    graph[i].add(j)
    graph[j].add(i)

# Calculate connected nodes and links
num_nodes_connected, num_links_connected = calculate_connected_nodes_and_links(graph, numNodes)

# Find the node with the maximum number of connected links
max_links_node = max(num_links_connected, key=num_links_connected.get)

# Output the result
print(max_links_node)