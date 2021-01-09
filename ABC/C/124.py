s = input()

odd = ''
even = ''
odd_count = 0
even_count = 0
for i in range(len(s)):
    if i % 2 == 0:
        odd = '0'
        even = '1'
    else:
        odd = '1'
        even = '0'

    if odd != s[i]:
        odd_count += 1
    elif even != s[i]:
        even_count += 1

print(min(odd_count, even_count))
