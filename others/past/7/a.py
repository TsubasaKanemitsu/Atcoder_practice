s = input()

odd = 0
even = 0
for i in range(len(s) - 1):
    if i % 2 == 0:
        odd += int(s[i])
    if i % 2 == 1:
        even += int(s[i])
num = (odd * 3 + even) % 10

if num == int(s[-1]):
    print("Yes")
else:
    print("No")