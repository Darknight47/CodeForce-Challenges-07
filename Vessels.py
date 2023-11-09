"""
------------- Link for the challenge: https://codeforces.com/problemset/problem/1872/A ------------

You have two vessels with water. The first vessel contains a grams of water, and the second vessel 
contains b grams of water. Both vessels are very large and can hold any amount of water.

You also have an empty cup that can hold up to c grams of water.

In one move, you can scoop up to c grams of water from any vessel and pour it into the other vessel. 
Note that the mass of water poured in one move does not have to be an integer.

What is the minimum number of moves required to make the masses of water in the vessels equal? 
Note that you cannot perform any actions other than the described moves.

Input
Each test contains multiple test cases. The first line contains the number of test cases t
(1 ≤ t ≤ 1000). The description of the test cases follows.

Each test case consists of a single line containing three integers a, b, and c 
(1 ≤ a, b, c ≤ 100) — the mass of water in the vessels and the capacity of the cup, respectively.

Output
For each test case, output a single number — the minimum number of moves required to make 
the masses of water in the vessels equal. It can be shown, that it is always possible.

Input:
6
3 7 2
17 4 3
17 17 1
17 21 100
1 100 1
97 4 3

Output:
1
3
0
1
50
16
"""
cases = int(input())
for i in range(cases):
    a, b, c = map(int, input().split())
    dec = max(a, b)
    inc = min(a, b)
    ans = 0
    while True:
        if(dec <= inc):
            break
        dec -= c
        inc += c
        ans += 1
    print(ans)