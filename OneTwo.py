"""
-------- Link for the challenge: https://codeforces.com/problemset/problem/1788/A ------------

You are given a sequence a1,a2,…,an. Each element of a is 1 or 2.

Find out if an integer k exists so that the following conditions are met.

1 ≤ k ≤ n−1, and a1⋅a2⋅…⋅ak = ak+1⋅ak+2⋅…⋅an.
If there exist multiple k that satisfy the given condition, print the smallest.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 100). 
Description of the test cases follows.

The first line of each test case contains one integer n (2 ≤ n ≤ 1000).

The second line of each test case contains n integers a1,a2,…,an (1≤a(i)≤2).

Output
For each test case, if there is no such k, print −1.

Otherwise, print the smallest possible k.

Input:
3
6
2 2 1 2 1 2
3
1 2 1
4
1 1 1 1

Output:
2
-1
1
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    lst = list(map(int, input().split()))
    tempSet = set(lst)
    twos = lst.count(2)
    half = twos // 2
    exist = True
    if(twos % 2 == 1):
        exist = False
    if(len(tempSet) == 1):
        tv = tempSet.pop()
        if(tv == 1):
            print(1)
        else:
            if(not exist):
                print(-1)
            else:
                print(sze // 2)
    else:
        ans = -1
        if(exist):
            for j in range(sze):
                temp = lst[j]
                if(temp == 2):
                    twos -= 1
                if(twos == half):
                    ans = j + 1
                    break
        print(ans)