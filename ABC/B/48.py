import math
a, b, x = list(map(int, input().split()))

b_sum = b // x
a_sum = (a - 1) // x

ans = b_sum - a_sum
print(ans)