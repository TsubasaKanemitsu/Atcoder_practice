a, b = list(map(int, input().split()))
result = a * b
if result % 2 == 1:
  print('Odd')
else:
  print('Even')