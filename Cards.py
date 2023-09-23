"""
------------ Link for the challenge: https://codeforces.com/problemset/problem/701/A -----------

There are n cards (n is even) in the deck. Each card has a positive integer written on it. 
n / 2 people will play new card game. At the beginning of the game each player gets two cards, 
each card is given to exactly one player.

Find the way to distribute cards such that the sum of values written of the cards will be equal for each player. 
It is guaranteed that it is always possible.

Input
The first line of the input contains integer n (2 ≤ n ≤ 100) — the number of cards in the deck. 
It is guaranteed that n is even.

The second line contains the sequence of n positive integers a1, a2, ..., an (1 ≤ ai ≤ 100), where a(i) 
is equal to the number written on the i-th card.

Output
Print n / 2 pairs of integers, the i-th pair denote the cards that should be given to the i-th player. 
Each card should be given to exactly one player. Cards are numbered in the order they appear in the input.

It is guaranteed that solution exists. If there are several correct answers, you are allowed to print any of them.

Input:
6
1 5 7 4 4 3

Output:
1 3
6 2
4 5
"""
sze = int(input())
unsorted_list = list(map(int, input().split()))
sorted_list = sorted(unsorted_list)
value_to_indices = {}
for index, value in enumerate(unsorted_list):
    if value not in value_to_indices:
        value_to_indices[value] = []
    value_to_indices[value].append(index)

for i in range(len(sorted_list) // 2):
    print(value_to_indices[sorted_list[i]].pop(0) + 1, value_to_indices[sorted_list[-(i+1)]].pop() + 1)