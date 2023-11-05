"""
-------------- Link for the challenge: https://codeforces.com/problemset/problem/1615/A ------------ 

There are n block towers in a row, where tower i has a height of a(i). 
You're part of a building crew, and you want to make the buildings look as nice as possible. 
In a single day, you can perform the following operation:

Choose two indices i and j (1 ≤ i, j ≤n; i≠j), and move a block from tower i to tower j. 
This essentially decreases a(i) by 1 and increases a(j) by 1.
You think the ugliness of the buildings is the height difference between the tallest and shortest buildings. 
Formally, the ugliness is defined as max(a)−min(a).

What's the minimum possible ugliness you can achieve, after any number of days?

Input
The first line contains one integer t (1 ≤ t ≤ 1000) — the number of test cases. Then t cases follow.

The first line of each test case contains one integer n (2 ≤ n ≤ 100) — the number of buildings.

The second line of each test case contains n space separated integers a1,a2,…,an 
(1≤ a(i) ≤ 10^7) — the heights of the buildings.

Output
For each test case, output a single integer — the minimum possible ugliness of the buildings.

Input:
3
3
10 10 10
4
3 2 1 2
5
1 2 3 1 5

Output:
0
0
1
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    lst = list(map(int, input().split()))
    tempSum = sum(lst)
    if(tempSum % sze == 0):
        print(0)
    else:
        print(1)