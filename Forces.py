"""
---------- Link for the challenge: https://codeforces.com/problemset/problem/1792/A -----------

Monocarp is playing a computer game. He's going to kill n monsters, the i-th of them has h(i) health.

Monocarp's character has two spells, either of which he can cast an arbitrary number of times (possibly, zero) 
and in an arbitrary order:

choose exactly two alive monsters and decrease their health by 1;
choose a single monster and kill it. When a monster's health becomes 0, it dies.

What's the minimum number of spell casts Monocarp should perform in order to kill all monsters?

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of testcases.

The first line of each testcase contains a single integer n
(1 ≤ n ≤ 100) — the number of monsters.

The second line contains n integers h1,h2,…,hn (1 ≤ h(i) ≤ 100) — the health of each monster.

The sum of n over all testcases doesn't exceed 2⋅10^4.

Output
For each testcase, print a single integer — the minimum number of spell casts Monocarp 
should perform in order to kill all monsters.

Input:
3
4
1 2 1 2
3
2 4 2
5
1 2 3 4 5

Output:
3
3
5
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    lst = sorted(map(int, input().split()))
    tempSet = set(lst)
    ans = 0
    if(len(tempSet) == sze):
        ans = sze
    else:
        ones = lst.count(1)
        temp = 0
        if(ones % 2 == 0):
            temp = ones // 2
        else:
            temp = ((ones - 1) // 2) + 1
        ans = (sze - ones) + temp
    print(ans)