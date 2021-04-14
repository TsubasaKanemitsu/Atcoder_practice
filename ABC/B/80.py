n = input()
digit_sum = sum(map(int, list(n)))
num_n = int(n)

if num_n % digit_sum == 0:
    print("Yes")
else:
    print("No")