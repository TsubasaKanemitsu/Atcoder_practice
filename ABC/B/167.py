A, B, C, k = list(map(int, input().split()))
ans = 0

if k <= A:
    ans = k
elif k <= A + B:
    ans = A
else:
    ans = A - (k - A - B)

        
print(ans)
