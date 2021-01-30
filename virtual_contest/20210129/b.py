s = list(input())

zero = s.count('0')
one = s.count('1')
count = min(zero, one)


print(count * 2)