N = int(input())

L = list(map(int, input().split()))

mx_val = max(L)
L.remove(mx_val)
sum_val = sum(L)

if mx_val < sum_val:
    print("Yes")
else:
    print("No")