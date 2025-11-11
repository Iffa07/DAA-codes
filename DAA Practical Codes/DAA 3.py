import time
import sys

# Function to solve Fractional Knapsack problem
def fractional_knapsack(values, weights, capacity):
    n = len(values)

    # Step 1: Calculate value-to-weight ratios
    ratio = [(values[i] / weights[i], values[i], weights[i]) for i in range(n)]

    # Step 2: Sort items by ratio in descending order (Greedy choice)
    ratio.sort(reverse=True)

    total_value = 0.0  # Total value accumulated
    remaining_capacity = capacity

    print("\nItem\tValue\tWeight\tValue/Weight")
    for r, v, w in ratio:
        print(f"{values.index(v)+1}\t{v}\t{w}\t{r:.2f}")

    print("\nItems taken into the knapsack:")

    # Step 3: Pick items based on ratio
    for r, v, w in ratio:
        if remaining_capacity == 0:
            break

        if w <= remaining_capacity:
            # Take the entire item
            total_value += v
            remaining_capacity -= w
            print(f"Took full item (value={v}, weight={w})")
        else:
            # Take fractional part of the item
            fraction = remaining_capacity / w
            total_value += v * fraction
            print(f"Took {fraction:.2f} fraction of item (value={v}, weight={w})")
            remaining_capacity = 0

    return total_value


# ------------------ MAIN PROGRAM ------------------

# Step 1: User input
n = int(input("Enter number of items: "))
values = []
weights = []

for i in range(n):
    print(f"\nItem {i+1}:")
    values.append(float(input("Enter value: ")))
    weights.append(float(input("Enter weight: ")))

capacity = float(input("\nEnter capacity of knapsack: "))

# Step 2: Measure time
start_time = time.time()
max_value = fractional_knapsack(values, weights, capacity)
end_time = time.time()

# Step 3: Approximate memory usage
mem_usage = sys.getsizeof(values) + sys.getsizeof(weights) + sys.getsizeof(max_value)

# Step 4: Display results
print("\n---------------------------------------")
print(f"Maximum value in knapsack = {max_value:.2f}")
print(f"Execution Time: {end_time - start_time:.6f} seconds")
print(f"Approx. Memory Used: {mem_usage} bytes")

# Step 5: Display theoretical complexity
print("\n---------------------------------------")
print("Theoretical Complexity Analysis:")
print("Time Complexity: O(n log n)  -> due to sorting of ratios")
print("Space Complexity: O(n)       -> for storing ratio list and input arrays")









'''
OUTPUT1:-

Enter number of items: 3

Item 1:
Enter value: 60
Enter weight: 10

Item 2:
Enter value: 100
Enter weight: 20

Item 3:
Enter value: 120
Enter weight: 30

Enter capacity of knapsack: 50

Item	Value	Weight	Value/Weight
1	60.0	10.0	6.00
2	100.0	20.0	5.00
3	120.0	30.0	4.00

Items taken into the knapsack:
Took full item (value=60.0, weight=10.0)
Took full item (value=100.0, weight=20.0)
Took 0.67 fraction of item (value=120.0, weight=30.0)

---------------------------------------
Maximum value in knapsack = 240.00
Execution Time: 0.000000 seconds
Approx. Memory Used: 200 bytes

---------------------------------------
Theoretical Complexity Analysis:
Time Complexity: O(n log n)  -> due to sorting of ratios
Space Complexity: O(n)       -> for storing ratio list and input arrays

'''