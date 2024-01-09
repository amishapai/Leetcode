'''
Monocarp is a great solver of adhoc problems. Recently, he participated in an Educational Codeforces Round, and gained rating!

Monocarp knew that, before the round, his rating was a. After the round, it increased to b(b>a). He wrote both values one after another to not forget them.

However, he wrote them so close to each other, that he can't tell now where the first value ends and the second value starts.

Please, help him find some values a and b such that

neither of them has a leading zero
both of them are strictly greater than 0
b>a
they produce the given value ab when written one after another.
If there are multiple answers, you can print any of them.

Input Format

The first line contains a single integer t (1≤t≤10000) — the number of testcases.

The only line of each testcase consists of a single string ab of length from 2 to 8 that:

consists only of digits;
doesn't start with a zero.
Constraints

time limit per test: 2 seconds memory limit per test: 256 megabytes

Output Format

For each testcase, determine if such values a and b exist. If they don't, print -1. Otherwise, print two integers a and b.

If there are multiple answers, you can print any of them.
'''

def find_values(ab):
    n = len(ab)
    for i in range(1, n):
        a_str = ab[:i]
        b_str = ab[i:]

        if b_str[0] != '0':
            a = int(a_str)
            b = int(b_str)

            if a > 0 and b > 0 and b > a:
                return a, b

    return -1, -1

def main():
    t = int(input())
    for _ in range(t):
        ab = input().strip()
        a, b = find_values(ab)
        if a == -1:
            print(-1)
        else:
            print(a, b)

if __name__ == "__main__":
    main()
