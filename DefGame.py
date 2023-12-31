"""
---------- Link for the challenge: https://codeforces.com/problemset/problem/1081/A ------------

Chouti was doing a competitive programming competition. However, after having all the problems accepted, 
he got bored and decided to invent some small games.

He came up with the following game. The player has a positive integer n. 
Initially the value of n equals to v and the player is able to do the following operation 
as many times as the player want (possibly zero): 
choose a positive integer x that x < n and x is not a divisor of n, then subtract x from n. 
The goal of the player is to minimize the value of n in the end.

Soon, Chouti found the game trivial. Can you also beat the game?

Input
The input contains only one integer in the first line: v (1 ≤ v ≤ 10^9), the initial value of n.

Output
Output a single integer, the minimum value of n the player can get.

Input:
8
Output:
1
"""
n = int(input())
if(n == 2):
    print(2)
else:
    print(1)