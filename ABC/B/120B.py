A, B, K = list(map(int, input().split()))
num_list = []
for i in range(1, min(A, B) + 1):
    if A % i == 0 and B % i == 0:
        num_list.append(i)

print(num_list[-K])

# 両方割り切れる数値は最大公約数が最大となるので
# rangeの指定範囲はA, Bの最小の方で良い
