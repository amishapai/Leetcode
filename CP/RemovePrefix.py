'''
Polycarp was presented with some sequence of integers a of length n (1≤ai≤n). A sequence can make Polycarp happy only if it consists of different numbers (i.e. distinct numbers). In order to make his sequence like this, Polycarp is going to make some (possibly zero) number of moves.

In one move, he can:

1.remove the first (leftmost) element of the sequence. For example, in one move, the sequence [3,1,4,3] will produce the sequence [1,4,3], which consists of different numbers.

2.Determine the minimum number of moves he needs to make so that in the remaining sequence all elements are different. In other words, find the length of the smallest prefix of the given sequence a, after removing which all values in the sequence will be unique.

Input Format

The first line of the input contains a single integer t — the number of test cases.

Each test case consists of two lines.

The first line contains an integer n — the length of the given sequence a.

The second line contains n integers a1,a2,…,an — elements of the given sequence a.

It is guaranteed that the sum of n values over all test cases does not exceed 2*10^5.

Constraints

1≤t≤10^4 1≤n≤2*10^5 1≤ai≤n

Output Format

For each test case print your answer on a separate line — the minimum number of elements that must be removed from the beginning
of the sequence so that all remaining elements are different.
'''


t = int(input())
for i in range(t):
    a = 0
    n = int(input())
    st = input()
    lis = st.split(" ")
    ind = 0
    cut = False
    if len(lis) > 1:
        for j in range(n):
            for k in range(j+1,n):
                if(lis[j] == lis[k] and k > ind):
                    ind = j
                    cut = True
        if(cut == True):      
            for c in range(ind+1):
                lis.pop(0)
        
        print(n - len(lis))
    else:
        print(0)
