"""
------- Link for the challenge: https://codeforces.com/problemset/problem/1626/A ---------

You are given a string s, consisting of lowercase Latin letters. Every letter appears in it no more than twice.

Your task is to rearrange the letters in the string in such a way that for each pair of letters 
that appear exactly twice, the distance between the letters in the pair is the same. 
You are not allowed to add or remove letters.

It can be shown that the answer always exists. If there are multiple answers, print any of them.

Input
The first line contains a single integer t (1 ≤ t ≤ 10^3) — the number of testcases.

Each testcase consists of a non-empty string s, consisting of lowercase Latin letters. 
Every letter appears in the string no more than twice. 
The length of the string doesn't exceed 52.

Output
For each testcase, print a single string. Every letter should appear in it the same number of times 
as it appears in string s. For each pair of letters that appear exactly twice, 
the distance between the letters in the pair should be the same.

If there are multiple answers, print any of them.

Input:
3
oelhl
abcdcba
ac

Output:
hello
ababcdc
ac
"""
cases = int(input())
for i in range(cases):
    word = input()
    setWord = set(word)
    ans = ""
    for j in setWord:
        count = word.count(j)
        for w in range(count):
            ans += j
    print(ans)