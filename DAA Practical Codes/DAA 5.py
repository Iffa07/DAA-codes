import time
import sys

def print_board(board):
    n = len(board)
    for r in range(n):
        print(' '.join('Q' if board[r][c] == 1 else '.' for c in range(n)))
    print()

def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, row, n, solutions, counters):
    counters["calls"] += 1

    if row == n:
        solutions.append([r[:] for r in board])
        return

    # Skip the row that already has the first queen
    if 1 in board[row]:
        solve_nqueens(board, row + 1, n, solutions, counters)
        return

    for col in range(n):
        counters["tries"] += 1
        if is_safe(board, row, col, n):
            board[row][col] = 1
            counters["placed"] += 1
            solve_nqueens(board, row + 1, n, solutions, counters)
            board[row][col] = 0
            counters["backtracks"] += 1


# ---------------- MAIN PROGRAM ----------------
n = int(input("Enter the number of queens (N): "))

board = [[0] * n for _ in range(n)]
r = int(input(f"Enter the row index (0 to {n-1}) for first queen: "))
c = int(input(f"Enter the column index (0 to {n-1}) for first queen: "))

board[r][c] = 1

solutions = []
counters = {"calls": 0, "tries": 0, "placed": 0, "backtracks": 0}

# Measure time
start_time = time.time()
solve_nqueens(board, 0, n, solutions, counters)
end_time = time.time()

# Memory usage
mem_usage = (
    sys.getsizeof(board)
    + sys.getsizeof(solutions)
    + sys.getsizeof(counters)
)

# Display results
if not solutions:
    print("\nNo solution exists for this configuration.")
else:
    print(f"\nTotal Solutions Found: {len(solutions)}")
    for idx, sol in enumerate(solutions, 1):
        print(f"\nSolution #{idx}:")
        print_board(sol)

print("--------------------------------------")
print("🔍 EMPIRICAL ANALYSIS:")
print(f"Recursive Calls Made: {counters['calls']}")
print(f"Placement Attempts:   {counters['tries']}")
print(f"Successful Placements:{counters['placed']}")
print(f"Backtracks:           {counters['backtracks']}")
print(f"Execution Time:       {end_time - start_time:.6f} seconds")
print(f"Approx. Memory Used:  {mem_usage} bytes")

print("\n--------------------------------------")
print("THEORETICAL COMPLEXITY ANALYSIS:")
print("Time Complexity (Worst Case): O(N!)")
print("  - Each queen can be placed in up to N columns per row.")
print("  - Backtracking explores many permutations (pruned by safety checks).")
print("Space Complexity: O(N^2) for the board + O(N) recursion stack")
print("  => Overall Space Complexity: O(N^2)")


'''
OUTPUT:-

Enter the number of queens (N): 4
Enter the row index (0 to 3) for first queen: 0
Enter the column index (0 to 3) for first queen: 1

Total Solutions Found: 1

Solution #1:
. Q . .
. . . Q
Q . . .
. . Q .

--------------------------------------
 EMPIRICAL ANALYSIS:
Recursive Calls Made: 20
Placement Attempts:   36
Successful Placements:8
Backtracks:           8
Execution Time:       0.000452 seconds
Approx. Memory Used:  672 bytes

--------------------------------------
 THEORETICAL COMPLEXITY ANALYSIS:
Time Complexity (Worst Case): O(N!)
  - Each queen can be placed in up to N columns per row.
  - Backtracking explores many permutations (pruned by safety checks).
Space Complexity: O(N^2) for the board + O(N) recursion stack
  => Overall Space Complexity: O(N^2)


'''