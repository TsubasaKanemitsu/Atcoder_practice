n = int(input())

A = list(map(int, input().split()))
winner = A.copy()
for i in range(n - 1):
    temp_winner = []
    for j in range(0, 2 ** (n - i - 1)):
        if winner[2 * j + 1] > winner[2 * j]:
            temp_winner.append(winner[2 * j + 1])
        else:
            temp_winner.append(winner[2 * j])
    winner = temp_winner
val = min(winner)

index = A.index(val) + 1
print(index)