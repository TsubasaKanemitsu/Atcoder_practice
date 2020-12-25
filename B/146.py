n = int(input())
s = list(input())

for i in range(len(s)):
    ord_s = ord(s[i]) + n
    if ord_s > 90:
        ord_s = ord_s - 90 + 64
    s[i] = chr(ord_s)

print(''.join(s))