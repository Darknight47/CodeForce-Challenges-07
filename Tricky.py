"""
----------- Link for the challenge: https://codeforces.com/problemset/problem/598/A ----------

In this problem you are to calculate the sum of all integers from 1 to n, 
but you should take all powers of two with minus in the sum.

For example, for n = 4 the sum is equal to  - 1 - 2 + 3 - 4 =  - 4, because 1, 2 and 4 are 20, 21 and 22 respectively.

Calculate the answer for t values of n.

Input
The first line of the input contains a single integer t (1 ≤ t ≤ 100) — the number of values of n to be processed.

Each of next t lines contains a single integer n (1 ≤ n ≤ 10^9).

Output
Print the requested sum for each of t integers n given in the input.

Input:
2
4
1000000000

Output:
-4
499999998352516354
"""
cases = int(input())
for i in range(cases):
    n = int(input())
    total_sum = n * (n + 1) // 2
    i = 1
    sum_of_powers_of_2 = 0
    while i <= n:
        sum_of_powers_of_2 += i
        i *= 2
    print(total_sum - 2 * sum_of_powers_of_2)