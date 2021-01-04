K = int(input())

a = 0
mod = 0

result = -1
for i in range(1, K + 1):
    # print((10 * a + 7))
    a = (10 * a + 7) % K
    print(a)
    # if a == 0:
    #     result = i
    #     break
print(result)
