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


# Recursive version (prints series and nth Fibonacci number)
def recursive_series_and_number(n):
    series = []
    for i in range(n):
        series.append(fibonacci_recursive(i))
    print("\nRecursive Fibonacci Series:")
    print(series)
    print(f"Recursive {n}th Fibonacci Number: {series[-1]}")


# Iterative version (prints series and nth Fibonacci number)
def iterative_series_and_number(n):
    series = fibonacci_iterative(n)
    print("\nIterative Fibonacci Series:")
    print(series)
    print(f"Iterative {n}th Fibonacci Number: {series[-1]}")


# Main Program
n = int(input("Enter the number of terms: "))

iterative_series_and_number(n)
recursive_series_and_number(n)
