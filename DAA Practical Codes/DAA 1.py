import time
import sys

# Recursive Fibonacci
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Iterative Fibonacci
def fibonacci_iterative(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


# Recursive version (with time and memory)
def recursive_analysis(n):
    start_time = time.time()
    result = []
    for i in range(n):
        result.append(fibonacci_recursive(i))
    end_time = time.time()
    total_time = end_time - start_time
    mem_usage = sys.getsizeof(result)

    print("\nRecursive Fibonacci Series:")
    print(result)
    print(f"Time Taken: {total_time:.6f} seconds")
    print(f"Approx. Memory Used: {mem_usage} bytes")


# Iterative version (with time and memory)
def iterative_analysis(n):
    start_time = time.time()
    result = fibonacci_iterative(n)
    end_time = time.time()
    total_time = end_time - start_time
    mem_usage = sys.getsizeof(result)

    print("\nIterative Fibonacci Series:")
    print(result)
    print(f"Time Taken: {total_time:.6f} seconds")
    print(f"Approx. Memory Used: {mem_usage} bytes")


# Main Program
n = int(input("Enter the number of terms: "))

iterative_analysis(n)
recursive_analysis(n)
