n = int(input())
x_list = list(map(float, input().split()))
y_list = list(map(float, input().split()))

D1 = 0
D2 = 0
D3 = 0
Dt8 = 0

for i in range(n):
    D1 += abs(x_list[i] - y_list[i])
    D2 += abs(x_list[i] - y_list[i]) ** 2
    D3 += abs(x_list[i] - y_list[i]) ** 3
    temp_Dt8 = abs(x_list[i] - y_list[i])
    if Dt8 < temp_Dt8:
        Dt8 = temp_Dt8
D2 = D2 ** (1 / 2)
D3 = D3 ** (1 / 3)

print(D1)
print(D2)
print(D3)
print(Dt8)