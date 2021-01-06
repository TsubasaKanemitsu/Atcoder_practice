N, X = list(map(int, input().split()))
S = input()

for i in range(N):
    result = S[i]
    if result == "o":
        X += 1
    else:
        if X != 0:
            X -= 1
        else:
            pass

print(X)