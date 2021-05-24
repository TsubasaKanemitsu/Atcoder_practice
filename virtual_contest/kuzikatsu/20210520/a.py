n = [int(input()) for _ in range(4)]

ab = n[0:2]
cd = n[2:4]

ans = min(ab[0], ab[1]) + min(cd[0], cd[1])
print(ans)