"""
------------- Link for the challenge: https://codeforces.com/problemset/problem/1719/A ------------

Burenka and Tonya are playing an old Buryat game with a chip on a board of n×m cells.

At the beginning of the game, the chip is located in the lower left corner of the board. 
In one move, the player can move the chip to the right or up by any odd number of cells 
(but you cannot move the chip both to the right and up in one move). The one who cannot make a move loses.

Burenka makes the first move, the players take turns. Burenka really wants to win the game, 
but she is too lazy to come up with a strategy, so you are invited to solve the difficult task of finding it. 
Name the winner of the game (it is believed that Burenka and Tonya are masters of playing with chips, so they 
always move in the optimal way).

Input
The first line contains one integer t (1 ≤ t ≤ 10^4) — the number of test cases. 
The following is a description of the input data sets.

The only line of each test case contains two integers n and m (1 ≤ n,m ≤ 10^9) — the dimensions of the game board.

Output
For each test case print a single line — the name of the winner of the game ("Burenka" or "Tonya").

Input:
6
1 1
1 4
5 6
2 2
6 3
999999999 1000000000

Output:
Tonya
Burenka
Burenka
Tonya
Burenka
Burenka
"""
cases = int(input())
for i in range(cases):
    n, m = map(int, input().split())
    temp = n + m
    if(temp % 2 == 0):
        print("Tonya")
    else:
        print("Burenka")