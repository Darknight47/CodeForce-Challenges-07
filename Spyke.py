"""
--------- Link for the challenge: https://codeforces.com/problemset/problem/291/A -------------

Polycarpus is the director of a large corporation. There are n secretaries working for the corporation, 
each of them corresponds via the famous Spyke VoIP system during the day. We know that when two people call 
each other via Spyke, the Spyke network assigns a unique ID to this call, a positive integer session number.

One day Polycarpus wondered which secretaries are talking via the Spyke and which are not. 
For each secretary, he wrote out either the session number of his call or a 0 if this secretary wasn't 
talking via Spyke at that moment.

Help Polycarpus analyze these data and find out the number of pairs of secretaries that are talking. 
If Polycarpus has made a mistake in the data and the described situation could not have taken place, say so.

Note that the secretaries can correspond via Spyke not only with each other, but also with the people 
from other places. Also, Spyke conferences aren't permitted — that is, one call connects exactly two people.

Input
The first line contains integer n (1 ≤ n ≤ 10^3) — the number of secretaries in Polycarpus's corporation. 
The next line contains n space-separated integers: id1, id2, ..., idn (0 ≤ idi ≤ 10^9). 
Number idi equals the number of the call session of the i-th secretary, if the secretary is talking via Spyke, 
or zero otherwise.

Consider the secretaries indexed from 1 to n in some way.

Output
Print a single integer — the number of pairs of chatting secretaries, or -1 if Polycarpus's 
got a mistake in his records and the described situation could not have taken place.

Input:
6
0 1 7 1 7 10

Output:
2
"""
cases = int(input())
arr = list(map(int, input().split()))
diction = {}
for i in range(cases):
    tk = arr[i]
    if(tk != 0):
        if tk not in diction:
            diction[tk] = 1
        else:
            diction[tk] = diction[tk] + 1
ans = 0
for j in diction:
    tv = diction[j]
    if(tv > 2):
        ans = -1
        break
    elif(tv == 2):
        ans += 1
print(ans)