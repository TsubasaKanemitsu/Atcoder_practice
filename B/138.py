n = int(input())
A = list(map(int, input().split()))

denominator = [1 / i for i in A]

ans = 1 / sum(denominator)

print(ans)