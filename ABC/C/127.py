n, m = list(map(int, input().split()))

L, R = [], []

for i in range(m):
    l, r = list(map(int, input().split()))
    L.append(l)
    R.append(r)

low = L[0]
high = R[0]

for i in range(1, m):
    if low < L[i]:
        low = L[i]
    else:
        pass
    if high > R[i]:
        high = R[i]
    else:
        pass
   
num = [i for i in range(low, high + 1)]
print(len(num))
