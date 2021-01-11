n = int(input())

sum_val = 0
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(n):
    sum_val += a[i] * b[i]
    
if sum_val == 0:
    print("Yes")
else:
    print("No")