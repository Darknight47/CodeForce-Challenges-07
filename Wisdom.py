"""
----------- Link for the challenge: https://codeforces.com/problemset/problem/1850/B -------------

In the game show "Ten Words of Wisdom", there are n participants numbered from 1 to n, 
each of whom submits one response. 
The i-th response is a(i) words long and has quality b(i). 
No two responses have the same quality, and at least one response has length at most 10.

The winner of the show is the response which has the highest quality out of all responses 
that are not longer than 10 words. Which response is the winner?

Input
The first line contains a single integer t (1 ≤ t ≤ 100) — the number of test cases.

The first line of each test case contains a single integer n (1 ≤ n ≤ 50) — the number of responses.

Then n lines follow, the i-th of which contains two integers a(i) and b(i) (1 ≤ a(i), b(i) ≤ 50) — 
the number of words and the quality of the i-th response, respectively.

Additional constraints on the input: in each test case, at least one value of i satisfies a(i) ≤ 10, 
and all values of b(i) are distinct.

Output
For each test case, output a single line containing one integer x (1 ≤ x ≤ n) — 
the winner of the show, according to the rules given in the statement.

It can be shown that, according to the constraints in the statement, exactly one winner exists for each test case.

Input:
3
5
7 2
12 5
9 3
9 4
10 1
3
1 2
3 4
5 6
1
1 43

Output:
4
3
1
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    maxQuality = 0
    ans = 0
    for j in range(sze):
        leng, quality = map(int, input().split())
        if(leng <= 10):
            if(quality > maxQuality):
                maxQuality = quality
                ans = j + 1
    print(ans)