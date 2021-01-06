k, x = list(map(int, input().split()))
ans = []
if x - (k - 1) >= -1000000 and x + k <= 1000000:
    ans = [i for i in range(x - k + 1, x + k)]
elif x - (k - 1) < -1000000:
    print("jlsdkf")
    diff = abs(x - k  + 1000000)
    high =  - 1000000 + diff
    print(high)
    ans = [i for i in range(-1000000, high)]
    print(ans)
elif x + k > 1000000:
    diff = abs(x + k - 1  - 1000000)
    print(diff)
    ans = [i for i in range(1000000 - diff, 1000001)]
else:
    pass

for i in range(len(ans)):
    print(ans[i], '', end='')
print()