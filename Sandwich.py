"""
---------- Link for the challenge: https://codeforces.com/problemset/problem/1849/A -------------

Monocarp always starts his morning with a good ol' sandwich. Sandwiches Monocarp makes always consist of bread, 
cheese and/or ham.

A sandwich always follows the formula:

a piece of bread
a slice of cheese or ham
a piece of bread
…
a slice of cheese or ham
a piece of bread

So it always has bread on top and at the bottom, and it alternates between bread and filling, 
where filling is a slice of either cheese or ham. 
Each piece of bread and each slice of cheese or ham is called a layer.

Today Monocarp woke up and discovered that he has b pieces of bread, c slices of cheese and h slices of ham. 
What is the maximum number of layers his morning sandwich can have?

Input
The first line contains a single integer t (1 ≤ t ≤ 1000) — the number of testcases.

Each testcase consists of three integers b,c and h (2 ≤ b ≤ 100; 1≤c,h ≤ 100) — 
the number of pieces of bread, slices of cheese and slices of ham, respectively.

Output
For each testcase, print a single integer — the maximum number of layers Monocarp's morning sandwich can have.

Input:
3
2 1 1
10 1 2
3 7 8

Output:
3
7
5
"""
cases = int(input())
for i in range(cases):
    b, c, h = map(int, input().split())
    b -= 2
    c -= 1
    ans = 3
    temp = min(b, (c + h)) * 2
    ans += temp
    print(ans)    