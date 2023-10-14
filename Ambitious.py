"""
------------ Link for the challenge: https://codeforces.com/problemset/problem/1866/A -------------
Chaneka, Pak Chanek's child, is an ambitious kid, so Pak Chanek gives her the following problem to test her ambition.

Given an array of integers [A1,A2,A3,…,AN]. 
In one operation, Chaneka can choose one element, then increase or decrease the element's value by 1. 
Chaneka can do that operation multiple times, even for different elements.

What is the minimum number of operations that must be done to make it such that A1×A2×A3×…×AN=0?

Input
The first line contains a single integer N (1 ≤ N ≤ 10^5).

The second line contains N integers A1,A2,A3,…,AN (−10^5 ≤ A(i) ≤ 10^5).

Output
An integer representing the minimum number of operations that must be done to make it such that A1×A2×A3×…×AN=0.

Input:
3
2 -6 5

Output:
2
"""
sze = int(input())
arr = sorted(list(map(int, input().split())))
positives = []
negatives = []
zero = False
for i in range(sze):
    temp = arr[i]
    if(temp > 0):
        positives.append(temp)
    elif(temp < 0):
        negatives.append(temp)
    else:
        zero = True
        break
if(zero):
    print(0)
else:
    if(len(negatives) > 0 and len(positives) > 0):
        print(positives[0] if(positives[0] < abs(negatives[len(negatives) - 1])) else negatives[len(negatives) - 1] * -1)
    elif(len(negatives) == 0 and len(positives) > 0):
        print(positives[0])
    else:
        print(negatives[len(negatives) - 1] * -1)