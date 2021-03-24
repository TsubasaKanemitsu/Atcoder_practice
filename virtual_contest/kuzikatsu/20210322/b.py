n, k = list(map(int, input().split()))

l = list(map(int, input().split()))

l.sort(reverse=True)

ans = sum(l[0:k])
print(ans)