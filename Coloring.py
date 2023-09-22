"""
---------- Link for the challenge: https://codeforces.com/problemset/problem/1843/A --------------

Sasha found an array a consisting of n integers and asked you to paint elements.

You have to paint each element of the array. You can use as many colors as you want, 
but each element should be painted into exactly one color, and for each color, there should be at least 
one element of that color.

The cost of one color is the value of max(S)−min(S), where S is the sequence of elements of that color. 
The cost of the whole coloring is the sum of costs over all colors.

For example, suppose you have an array a=[1,5,6,3,4], and you painted its elements into two colors as follows: 
elements on positions 1, 2and 5have color 1; 
elements on positions 3 and 4have color 2. Then:

the cost of the color 1 is max([1,5,4])−min([1,5,4])=5−1=4;
the cost of the color 2 is max([6,3])−min([6,3])=6−3=3; the total cost of the coloring is 7.
For the given array a, you have to calculate the maximum possible cost of the coloring.

Input
The first line contains one integer t (1 ≤ t ≤ 1000) — the number of test cases.

The first line of each test case contains a single integer n (1 ≤ n ≤ 50) — length of a.

The second line contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 50) — array a.

Output
For each test case output the maximum possible cost of the coloring.

Input:
6
5
1 5 6 3 4
1
5
4
1 6 3 9
6
1 13 9 3 7 2
4
2 2 2 2
5
4 5 2 2 3

Output:
7
0
11
23
0
5
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    arr = sorted(map(int, input().split()))
    tempSet = set(arr)
    pairs = 0
    ans = 0
    pairs = sze // 2
    if(sze == 0 or len(tempSet) == 0):
        ans = 0
    else:
        firstIndx = 0
        lastIndx = sze - 1        
        while pairs > 0:
            tempElem1 = arr[firstIndx]
            tempElem2 = arr[lastIndx]
            tempDiff = tempElem2 - tempElem1
            ans += tempDiff
            pairs -= 1
            firstIndx += 1
            lastIndx -= 1
    print(ans)