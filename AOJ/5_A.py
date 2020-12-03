result = 1
count = 0
H = []
W = []
while result > 0:
    h, w = list(map(int, input().split()))
    if h + w != 0:
        H.append(h)
        W.append(w)
    else:
        break
    count += 1

for c in range(count):
    for i in range(H[c]):
        for j in range(W[c]):
            print('#', end="")
            
        print()
    print()