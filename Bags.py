"""
Dawid has four bags of candies. The i-th of them contains a(i) candies. 
Also, Dawid has two friends. He wants to give each bag to one of his two friends. 
Is it possible to distribute the bags in such a way that each friend receives the same amount of candies in total?

Note, that you can't keep bags for yourself or throw them away, each bag should be given to one of the friends.

Input
The only line contains four integers a1, a2, a3 and a4 (1 ≤ a(i) ≤ 100) — the numbers of candies in each bag.

Output
Output YES if it's possible to give the bags to Dawid's friends so that both friends receive the same 
amount of candies, or NO otherwise. Each character can be printed in any case (either uppercase or lowercase).

Input:
1 7 11 5

Output:
YES
"""
a, b, c, d = map(int, input().split())
ab = a + b
cd = c + d
ac = a + c
bd = b + d
ad = a + d
bc = b + c

abc = a + b + c
abd = a + b + d
bcd = b + c + d
acd = a + c + d
if((ab == cd) or (ac == bd) or (ad == bc)):
    print("YES")
elif((abc == d) or (abd == c) or (bcd == a) or (acd == b)):
    print("YES")
else:
    print("NO")