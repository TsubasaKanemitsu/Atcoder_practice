count = 1
result = []

while count > 0:
    number = str(input())
    number = list(map(int, number))
    if sum(number) > 0:
        result.append(sum(number))
    else:
        break
for i in range(len(result)):
    print(result[i])