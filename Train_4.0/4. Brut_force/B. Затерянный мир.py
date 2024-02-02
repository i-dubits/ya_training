
def isSafe(board, row, col, n):
    for i in range(col):
        if board[i] == row:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[j] == i:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[j] == i:
            return False

    return True

def solveNQUtil(board, col, n):
    if col >= n:
        return 1

    count = 0
    for i in range(n):
        if isSafe(board, i, col, n):
            board[col] = i
            count += solveNQUtil(board, col + 1, n)
            # backtrack
            board[col] = -1 

    return count

def solveDinosaurProblem(n):
    board = [-1] * n
    return solveNQUtil(board, 0, n)

with open('input.txt', 'r') as f:
    N = int(f.readline().strip())
    
print(solveDinosaurProblem(N))
