"""
-------- Link for the challenge: https://codeforces.com/problemset/problem/1061/A -----------

You have unlimited number of coins with values 1,2,…,n. 
You want to select some set of coins having the total value of S.

It is allowed to have multiple coins with the same value in the set. 
What is the minimum number of coins required to get sum S?

Input
The only line of the input contains two integers n and S (1 ≤ n ≤ 100000, 1 ≤ S ≤ 10^9)

Output
Print exactly one integer — the minimum number of coins required to obtain sum S.

Input:
5 11

Output:
3
"""
n, s = map(int, input().split())
founded = False
ans = 0
while not founded:
    remainder = s % n
    s = s // n
    ans += s
    if(remainder == 0):
        break
    elif(remainder > 0 and remainder < n):
        ans += 1
        founded = True
print(ans)