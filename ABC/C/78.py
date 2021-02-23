# わからなかった
n, m = list(map(int, input().split()))

y = (1900 * m + 100 * (n - m)) * 2 ** m
print(y)