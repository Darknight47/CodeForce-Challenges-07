"""
There's a chessboard of size n×n. m rooks are placed on it in such a way that:

1. no two rooks occupy the same cell;
2. no two rooks attack each other.

A rook attacks all cells that are in its row or column.

Is it possible to move exactly one rook (you can choose which one to move) into a different cell so that 
no two rooks still attack each other? A rook can move into any cell in its row or column if no other rook 
stands on its path.

Input
The first line contains a single integer t (1 ≤ t ≤ 2000) — the number of testcases.

The first line of each testcase contains two integers n and m (1 ≤ n,m ≤8) — 
the size of the chessboard and the number of the rooks.

The i-th of the next m lines contains two integers x(i) and y(i) (1≤ x(i), y(i) ≤n) — 
the position of the i-th rook: x(i) is the row and y(i) is the column.

No two rooks occupy the same cell. No two rooks attack each other.

Output
For each testcase, print "YES" if it's possible to move exactly one rook into a different cell so that 
no two rooks still attack each other. Otherwise, print "NO".

Input:
2
2 2
1 2
2 1
3 1
2 2

Output:
NO
YES
"""
cases = int(input())
for i in range(cases):
    n, rooks = map(int, input().split())
    arr = []
    for j in range(rooks):
        t1, t2 = map(int, input().split())
        tempTuple = (t1, t2)
        arr.append(tempTuple)
    if(rooks < n):
        print("YES")
    else:
        print("NO")
        