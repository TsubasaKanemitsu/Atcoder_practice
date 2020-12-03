result = 1
count = 0
H = []
W = []

while result > 0:
    h, w = list(map(int, input().split()))
    H.append(h)
    W.append(w)
    if H[count] + W[count] > 0:
        count += 1
    else:
        result = -1

for c in range(count + 1):
    if H[c] + W[c] > 0:
        for i in range(H[c]):
            for j in range(W[c]):
                if i % 2 == 0 and j % 2 == 0:
                    print('#', end='')
                elif i % 2 == 0 and j % 2 == 1:
                    print('.', end='')
                elif i % 2 == 1 and j % 2 == 0:
                    print('.', end='')
                else:
                    print('#', end='')
            print()
        print()