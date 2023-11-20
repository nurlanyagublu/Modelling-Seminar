#G72RIJ #python3

#This code will find a link to sever in a way that prevents the Bobnet agent from reaching an exit gateway in its current 
#sub-network.
#It does this by checking if severing a link would disconnect the current node from an exit gateway.
#If so, it severs that link. If not, it severs any random link to maintain control over the network.


import sys

# Parse the initialization data
n, l, e = map(int, input().split())
links = []
for i in range(l):
    n1, n2 = map(int, input().split())
    links.append((n1, n2))
exit_gateways = []
for i in range(e):
    ei = int(input())
    exit_gateways.append(ei)

# Function to find a link to sever
def find_link_to_sever(current_node):
    for link in links:
        n1, n2 = link
        # Check if severing this link disconnects the current node from an exit gateway
        if (n1 == current_node and n2 in exit_gateways) or (n2 == current_node and n1 in exit_gateways):
            return n1, n2
    # If no such link is found, sever any random link
    return links[0]

# Game loop
while True:
    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn

    # Find a link to sever
    c1, c2 = find_link_to_sever(si)

    # Output the indices of the nodes to sever the link
    print(f"{c1} {c2}")

