"""
------------ Link for the challenge: https://codeforces.com/problemset/problem/1549/A -----------

Gregor is learning about RSA cryptography, and although he doesn't understand how RSA works, 
he is now fascinated with prime numbers and factoring them.

Gregor's favorite prime number is P. Gregor wants to find two bases of P. 
Formally, Gregor is looking for two integers a and b which satisfy both of the following properties.

P mod a = P mod b, where x mod y denotes the remainder when x is divided by y, and 2 ≤ a < b ≤ P.
Help Gregor find two bases of his favorite prime number!

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 1000).

Each subsequent line contains the integer P (5 ≤ P ≤ 10^9), with P guaranteed to be prime.

Output
Your output should consist of t lines. Each line should consist of two integers a and b (2 ≤ a < b ≤ P). 
If there are multiple possible.

Input:
2
17
5

Output:
3 5
2 4
"""
cases = int(input())
for i in range(cases):
    p = int(input())
    print(2, (p-1))