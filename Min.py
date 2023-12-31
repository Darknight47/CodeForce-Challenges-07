"""
--------- Link for the challenge: https://codeforces.com/problemset/problem/1680/A --------------

An array is beautiful if both of the following two conditions meet:

there are at least l1 and at most r1 elements in the array equal to its minimum; 
there are at least l2 and at most r2 elements in the array equal to its maximum.
For example, the array [2,3,2,4,4,3,2] has 3 elements equal to its minimum 
(1-st, 3-rd and 7-th) and 2elements equal to its maximum (4-th and 5-th).

Another example: the array [42,42,42] has 3 elements equal to its minimum and 3 elements equal to its maximum.

Your task is to calculate the minimum possible number of elements in a beautiful array.

Input
The first line contains one integer t (1 ≤ t ≤ 5000) — the number of test cases.

Each test case consists of one line containing four integers l1, r1, l2 and r2 
(1 ≤ l1 ≤ r1 ≤ 50; 1 ≤ l2 ≤ r2 ≤ 50).

Output
For each test case, print one integer — the minimum possible number of elements in a beautiful array.

Input:
7
3 5 4 6
5 8 5 5
3 3 10 12
1 5 3 3
1 1 2 2
2 2 1 1
6 6 6 6

Output:
4
5
13
3
3
3
6
"""
cases = int(input())
for i in range(cases):
    l1, r1, l2, r2 = map(int, input().split())
    if max(l1, l2) <= min(r1, r2):
        print(max(l1, l2))
    else:
        print(l1 + l2)