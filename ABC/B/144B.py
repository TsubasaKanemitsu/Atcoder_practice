N = int(input())

answer = "No"
for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        if result == N:
            answer = "Yes"
            break

print(answer)
