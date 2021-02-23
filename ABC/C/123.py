# 23分
n = int(input())
person = [int(input()) for _ in range(5)]
min_val = min(person)
if min_val > n:
    print(5)
    exit()

if n % min_val == 0:
    ans = 5 + n // min_val - 1
else:
    ans = 5 + n // min_val

print(ans)