import time
import sys

def knapsack_01(values, weights, capacity, n):
    # Create DP table initialized with zeros
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]],
                               dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtrack to find which items are included
    selected_items = []
    res = dp[n][capacity]
    w = capacity
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == dp[i - 1][w]:
            continue
        else:
            selected_items.append(i)
            res -= values[i - 1]
            w -= weights[i - 1]

    selected_items.reverse()
    return dp[n][capacity], selected_items


# ------------------- MAIN PROGRAM -------------------
n = int(input("Enter number of items: "))

values = []
weights = []

for i in range(n):
    print(f"\nItem {i + 1}:")
    values.append(int(input("Enter value: ")))
    weights.append(int(input("Enter weight: ")))

capacity = int(input("\nEnter capacity of knapsack: "))

# Measure execution time
start_time = time.time()
max_value, selected_items = knapsack_01(values, weights, capacity, n)
end_time = time.time()

# Approximate memory usage
mem_usage = sys.getsizeof(values) + sys.getsizeof(weights)

# Display results
print("\n---------------------------------------")
print(f"Maximum value in knapsack = {max_value}")
print(f"Items included (by index): {selected_items}")
print(f"Execution Time: {end_time - start_time:.6f} seconds")
print(f"Approx. Memory Used: {mem_usage} bytes")

# Theoretical complexity
print("\n---------------------------------------")
print("Theoretical Complexity Analysis:")
print("Time Complexity: O(n * W)  -> where n = items, W = capacity")
print("Space Complexity: O(n * W) -> DP table of size (n+1) x (W+1)")






'''
OUTPUT:-
Enter number of items: 4

Item 1:
Enter value: 1
Enter weight: 1

Item 2:
Enter value: 4
Enter weight: 3

Item 3:
Enter value: 5
Enter weight: 4

Item 4:
Enter value: 7
Enter weight: 5

Enter capacity of knapsack: 7

---------------------------------------
Maximum value in knapsack = 9
Items included (by index): [2, 3]
Execution Time: 0.000000 seconds
Approx. Memory Used: 176 bytes

---------------------------------------
Theoretical Complexity Analysis:
Time Complexity: O(n * W)  -> where n = items, W = capacity
Space Complexity: O(n * W) -> DP table of size (n+1) x (W+1)


'''