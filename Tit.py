"""
------------- Link for the challenge: https://codeforces.com/problemset/problem/1516/A ------------

Given an array a of length n, you can do at most k operations of the following type on it:

choose 2 different elements in the array, add 1 to the first, and subtract 1 from the second. 
However, all the elements of a have to remain non-negative after this operation.
What is lexicographically the smallest array you can obtain?

An array x is lexicographically smaller than an array y if there exists an index i such 
that x(i) < y(i), and x(j) = y(j) for all 1 ≤ j < i. 
Less formally, at the first index i in which they differ, x(i) < y(i).

Input
The first line contains an integer t (1 ≤ t ≤20) – the number of test cases you need to solve.

The first line of each test case contains 2 integers n and k (2 ≤ n ≤ 100, 1 ≤ k ≤ 10000) — 
the number of elements in the array and the maximum number of operations you can make.

The second line contains n space-separated integers a1, a2, …, an (0 ≤ a(i) ≤ 100) — the elements of the array a.

Output
For each test case, print the lexicographically smallest array you can obtain after at most k operations.

Input:
2
3 1
3 1 4
2 10
1 0

Output:
2 1 5 
0 1 
"""
cases = int(input())
for i in range(cases):
    sze, actions = map(int, input().split())
    lst = list(map(int, input().split()))
    additions = 0
    for i in range(sze - 1):
        if actions <= 0:
            break
        diff = min(actions, lst[i])
        lst[i] -= diff
        actions -= diff
        additions += diff
    lst[-1] += additions
    print(*lst)