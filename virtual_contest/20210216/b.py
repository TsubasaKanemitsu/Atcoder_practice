A, B, C = list(map(int, input().split()))
K = int(input())

for i in range(K + 1):
    a = 2 ** i * A
    for j in range(K + 1):
        b = 2 ** j * B
        for k in range(K + 1):
            c = 2 ** k * C
            if i + j + k == K and c > b > a:
                print("Yes")
                exit()
print("No")