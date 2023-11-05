"""
----------- Link for the challenge: https://codeforces.com/problemset/problem/1705/A ------------

Mark is asked to take a group photo of 2n people. The i-th person has height h(i) units.

To do so, he ordered these people into two rows, the front row and the back row, each consisting of npeople. 
However, to ensure that everyone is seen properly, 
the j-th person of the back row must be at least x units taller than the j-th 
person of the front row for each j between 1 and n, inclusive.

Help Mark determine if this is possible.

Input
The first line contains one integer t (1 ≤ t ≤ 100) — the number of test cases. 
Each test case consists of two lines.

The first line of each test case contains two positive integers n and x (1 ≤ n ≤ 100, 1 ≤ x ≤ 10^3) — 
the number of people in each row and the minimum difference Mark wants.

The second line of each test case contains 2n positive integers h1,h2,…,h2n (1 ≤ h(i) ≤ 10^3) 
— the height of each person in units.

Note that the sum of n over all test cases is not bounded.

Output
For each test case, print a single line containing "YES" if Mark could arrange people 
satisfying his condition and "NO" otherwise.

You may print each letter in any case (for example, YES, Yes, yes, yEs will all be recognized as positive answers).

Input:
3
3 6
1 3 9 10 12 16
3 1
2 5 2 2 2 5
1 2
8 6

Output:
YES
NO
YES
"""
cases = int(input())
for i in range(cases):
    n, x = map(int, input().split())
    lst = sorted(list(map(int, input().split())))
    ok = True
    for j in range(0, n):
        temp1 = lst[j]
        for w in range(n, (2*n)):
            temp2 = lst[w]
            if(temp2 > 0):
                diff = temp2 - temp1
                if(diff < x):
                    ok = False
                else:
                    lst[w] = 0
                break
        if(not ok):
            break
    print("YES" if ok else "NO")