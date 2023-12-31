"""
---------- Link for the challenge: https://codeforces.com/problemset/problem/1780/A -------------

Today Hayato came home from school with homework.

In the assignment, Hayato was given an array a of length n. 
The task was to find 3 numbers in this array whose sum is odd. 
At school, he claimed that there are such 3 numbers, 
but Hayato was not sure, so he asked you for help.

Answer if there are such three numbers, and if so, output indices i, j, and ksuch that ai+aj+ak is odd.

The odd numbers are integers that are not divisible by 2: 1, 3, 5, and so on.

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases.

For each test case, the first line contains one integer n (3 ≤ n ≤ 300) — the length of a.

The second line contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 10^5) — the array a.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, in the first line print one word "YES" (without quotes) if there are 
3 numbers with an odd sum or "NO" (without quotes) if there are no such 3 numbers.

If the answer exists, then on the second line print 3 distinct integers i,j,k (1 ≤ i, j, k ≤ n) — 
the indices of the numbers. If there are several answers, output any.

Input:
6
3
1 1 1
4
1 1 2 2
3
1 2 3
5
1 4 5 1 2
4
2 6 2 4
5
5 6 3 2 1

Output:
YES
1 2 3
YES
3 4 1
NO
YES
1 3 4
NO
YES
1 3 5
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    odds = []
    evens = []
    sumOddExist = False
    for j in range(sze):
        tempNum = arr[j]
        if(tempNum % 2 == 1):
            odds.append(j + 1)
        else:
            evens.append(j + 1)
        if((len(odds) == 3) or (len(odds) >= 1 and len(evens) >= 2)):
            sumOddExist = True
            break
    if(sumOddExist):
        print("YES")
        if(len(odds) == 3):
            print(odds[0], odds[1], odds[2])
        else:
            print(odds[0], evens[0], evens[1])
    else:
        print("NO")