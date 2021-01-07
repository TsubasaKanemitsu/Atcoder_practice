n = int(input())

H = list(map(int, input().split()))
H.reverse()
for i in range(n - 1):
    if H[i] >= H[i + 1]:
        continue
    else:
        H[i + 1] = H[i + 1] - 1
        if H[i] >= H[i + 1]:
            continue
        else:
            print("No")
            exit(0)
print("Yes")