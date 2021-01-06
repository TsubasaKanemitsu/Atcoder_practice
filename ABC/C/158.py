a, b = list(map(int, input().split()))

x = 1
result = -1
while x <= 1000:
    ans_a = int(x * 0.08)
    ans_b = int(x * 0.10)
    
    if ans_a == a and ans_b == b:
        result = x
        break
    x += 1

print(result)