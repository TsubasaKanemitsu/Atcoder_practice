A, B = list(map(int, input().split()))

count = 0
for number in range(A, B + 1):
    reverse_number = ''.join(list(reversed(str(number))))
    if str(number) == reverse_number:
        count += 1

print(count)