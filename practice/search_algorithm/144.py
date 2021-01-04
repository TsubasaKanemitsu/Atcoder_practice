# 1分30秒
n = int(input())

result = "No"
for i in range(1, 10):
    for j in range(1, 10):
        if n == i * j:
            result = "Yes"
print(result)