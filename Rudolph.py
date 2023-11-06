"""
--------- Link for the challenge: https://codeforces.com/problemset/problem/1846/B -----------

Rudolph invented the game of tic-tac-toe for three players. It has classic rules, 
except for the third player who plays with pluses. Rudolf has a 3×3
field  — the result of the completed game. Each field cell contains either a cross, 
or a nought, or a plus sign, or nothing. 
The game is won by the player who makes a horizontal, vertical or diagonal row of 3's of their symbols.

Rudolph wants to find the result of the game. Either exactly one of the three players won or it ended in a draw. 
It is guaranteed that multiple players cannot win at the same time.

Input
The first line contains one integer t (1 ≤ t ≤ 10^4) — the number of test cases.

Each test case consists of three lines, each of which consists of three characters. 
The symbol can be one of four: "X" means a cross, "O" means a nought, "+" means a plus, 
"." means an empty cell.

Output
For each test case, print the string "X" if the crosses won, "O" if the noughts won, 
"+" if the pluses won, "DRAW" if there was a draw.

Input:
5
+X+
OXO
OX.
O+.
+OX
X+O
.XO
OX.
+++
O.+
X.O
+..
.++
X.O
+..

Output:
X
O
+
DRAW
DRAW
"""
def horizontal(s1, s2, s3):
    if(s1[0] == s1[1] == s1[2] and s1[0] != '.'):
        return True, s1[0]
    elif(s2[0] == s2[1] == s2[2] and s2[0] != '.'):
        return True, s2[0]
    elif(s3[0] == s3[1] == s3[2] and s3[0] != '.'):
        return True, s3[0]
    return False, "DRAW"
def vertical(s1, s2, s3):
    if(s1[0] == s2[0] == s3[0]and s1[0] != '.'):
        return True, s1[0]
    elif(s1[1] == s2[1] == s3[1] and s1[1] != '.'):
        return True, s1[1]
    elif(s1[2] == s2[2] == s3[2] and s1[2] != '.'):
        return True, s1[2]
    return False, "DRAW"
def leftDiagon(s1, s2, s3):
    if(s1[0] == s2[1] == s3[2] and s1[0] != '.'):
        return True, s1[0]
    return False, "DRAW"
def rightDiagon(s1, s2, s3):
    if(s1[2] == s2[1] == s3[0] and s1[2] != '.'):
        return True, s1[2]
    return False, "DRAW"

cases = int(input())
for i in range(cases):
    first = input()
    second = input()
    third = input()
    t1, ans1 = vertical(first, second, third)
    t2, ans2 = horizontal(first, second, third)
    t3, ans3 = leftDiagon(first, second, third)
    t4, ans4 = rightDiagon(first, second, third)
    if(t1):
        print(ans1)
    elif(t2):
        print(ans2)
    elif(t3):
        print(ans3)
    elif(t4):
        print(ans4)
    else:
        print("DRAW")    