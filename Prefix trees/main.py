import sys
import math

class TrieNode:
    def __init__(self):
        self.children = {}  # Child nodes for each digit
        self.is_end_of_number = False  # Marks the end of a phone number

class Trie:
    def __init__(self):
        self.root = TrieNode()  # Initialize the root node
    
    def insert(self, number):
        node = self.root
        for digit in number:
            if digit not in node.children:
                node.children[digit] = TrieNode()  # Create a new node for the digit
            node = node.children[digit]
        node.is_end_of_number = True  # Mark the end of the phone number
    
    def count_nodes(self):
        return self._count_nodes_recursive(self.root)
    
    def _count_nodes_recursive(self, node):
        count = 1  # Count this node
        for child in node.children.values():
            count += self._count_nodes_recursive(child)  # Recursively count child nodes
        return count

def find_longest_common_prefix(numbers):
    if not numbers:
        return ""
    numbers.sort()  # Sort the numbers to find the longest common prefix
    first = numbers[0]
    last = numbers[-1]
    length = min(len(first), len(last))
    i = 0
    # Find the longest common prefix among the sorted numbers
    while i < length and first[i] == last[i]:
        i += 1
    return first[:i]

def main():
    n = int(input())
    phone_numbers = [input() for _ in range(n)]

    trie = Trie()
    # Find and insert the longest common prefix into the trie
    common_prefix = find_longest_common_prefix(phone_numbers)
    if common_prefix:
        trie.insert(common_prefix)

    # Insert phone numbers into the trie, considering the common prefix
    for number in phone_numbers:
        if common_prefix and number.startswith(common_prefix):
            trie.insert(number[len(common_prefix):])
        else:
            trie.insert(number)

    # Count the number of nodes in the trie
    node_count = trie.count_nodes()
    print(node_count - 1)  # Excluding the root node

if __name__ == "__main__":
    main()
