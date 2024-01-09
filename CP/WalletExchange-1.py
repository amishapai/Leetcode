'''
Alice and Bob are bored, so they decide to play a game with their wallets. Alice has a coins in her wallet, while Bob has b coins in his wallet.

Both players take turns playing, with Alice making the first move. In each turn, the player will perform the following steps in order:

1) Choose to exchange wallets with their opponent, or to keep their current wallets.

2) Remove 1 coin from the player's current wallet. The current wallet cannot have 0 coins before performing this step.

The player who cannot make a valid move on their turn loses. If both Alice and Bob play optimally, determine who will win the game.

Input Format

Each test contains multiple test cases. The first line contains a single integer t(1≤t≤1000) — the number of test cases. The description of the test cases follows.

The first and only line of each test case contains two integers a and b(1≤a,b≤1000000000) — the number of coins in Alice's and Bob's wallets, respectively.

Constraints

time limit per test: 1 second memory limit per test: 256 megabytes

Output Format

For each test case, output "Alice" if Alice will win the game, and "Bob" if Bob will win the game.
'''

def find_winner(a, b):
    # Determine the winner based on the parity of the total number of coins
    total_coins = a + b
    if total_coins % 2 == 0:
        return "Bob"
    else:
        return "Alice"

def main():
    # Input processing
    t = int(input())
    
    for _ in range(t):
        a, b = map(int, input().split())
        winner = find_winner(a, b)
        print(winner)

if __name__ == "__main__":
    main()
