'''
You are given three digits a
, b
, c
. Two of them are equal, but the third one is different from the other two.

Find the value that occurs exactly once.

Input
The first line contains a single integer t
 (1≤t≤270
) — the number of test cases.

The only line of each test case contains three digits a
, b
, c
 (0≤a
, b
, c≤9
). Two of the digits are equal, but the third one is different from the other two.

Output
For each test case, output the value that occurs exactly once.
'''


num=int(input())
for i in range (0,num):
    dig=input()
    dig= ''.join(list(map(lambda x: x.strip(), dig.split())))
    c=[]
    dig=list(dig)
    if dig[0]==dig[1]:
        print(dig[2])
    elif dig[1]==dig[2]:
        print(dig[0])
    else:
        print(dig[1])
