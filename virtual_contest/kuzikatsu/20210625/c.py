a, b, c = map(int, input().split())

bc = pow(b, c, 4)
if bc == 0:
    bc = 4
ans = pow(a, bc, 10)
print(ans)