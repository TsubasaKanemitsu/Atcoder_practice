n = int(input())

std_num = 96

count = 1
amari = []
while n > 0:
    n -= 1
    word = chr(ord('a') + n % 26)
    amari.append(word)
    n = n // 26
    
print(''.join(amari[::-1]))
