import heapq
import time
import sys

# Node class for Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Less-than operator for heap comparisons
    def __lt__(self, other):
        return self.freq < other.freq


# Function to print Huffman Codes
def print_huffman_codes(root, code=""):
    if root is None:
        return
    if root.char is not None:  # Leaf node
        print(f"{root.char} -> {code}")
    print_huffman_codes(root.left, code + "0")
    print_huffman_codes(root.right, code + "1")


# Huffman Encoding Function
def huffman_encoding(characters, frequencies):
    heap = []

    # Step 1: Build initial heap
    for i in range(len(characters)):
        heapq.heappush(heap, Node(characters[i], frequencies[i]))

    # Step 2: Combine nodes until one remains
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        new_node = Node(None, left.freq + right.freq)
        new_node.left = left
        new_node.right = right

        heapq.heappush(heap, new_node)

    # Step 3: The remaining node is the root
    root = heapq.heappop(heap)

    print("\nHuffman Codes are:")
    print_huffman_codes(root)

    # Return root for memory estimation
    return root


# ---------------------- MAIN PROGRAM ----------------------

# User input
n = int(input("Enter number of characters: "))
characters = []
frequencies = []

print("\nEnter character and its frequency:")
for i in range(n):
    ch = input(f"Character {i+1}: ")
    freq = int(input(f"Frequency of {ch}: "))
    characters.append(ch)
    frequencies.append(freq)

print("\nCharacters:", characters)
print("Frequencies:", frequencies)

# Measure execution time
start_time = time.time()
root = huffman_encoding(characters, frequencies)
end_time = time.time()

# Approximate memory usage (heap + arrays + nodes)
mem_usage = sys.getsizeof(characters) + sys.getsizeof(frequencies) + sys.getsizeof(root)

# Results
print("\n---------------- RESULTS ----------------")
print(f"Execution Time: {end_time - start_time:.6f} seconds")
print(f"Approx. Memory Usage: {mem_usage} bytes")

# Complexity summary
print("\n---------------- COMPLEXITY ANALYSIS ----------------")
print("Time Complexity: O(n log n)")
print("Space Complexity: O(n)")










'''
Output:
Enter number of characters: 6

Enter character and its frequency:
Character 1: A
Frequency of A: 5
Character 2: B
Frequency of B: 9
Character 3: C
Frequency of C: 12
Character 4: D
Frequency of D: 13
Character 5: E
Frequency of E: 16
Character 6: F
Frequency of F: 45

Characters: ['A', 'B', 'C', 'D', 'E', 'F']
Frequencies: [5, 9, 12, 13, 16, 45]

Huffman Codes are:
F -> 0
C -> 100
D -> 101
A -> 1100
B -> 1101
E -> 111

---------------- RESULTS ----------------
Execution Time: 0.000995 seconds
Approx. Memory Usage: 248 bytes

---------------- COMPLEXITY ANALYSIS ----------------
Time Complexity: O(n log n)
Space Complexity: O(n)

'''