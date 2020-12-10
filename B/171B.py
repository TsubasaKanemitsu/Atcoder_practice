N, K = list(map(int, input().split()))

P = list(map(int, input().split()))
P.sort()

result = P[0:K]
answer = sum(result)

print(answer)