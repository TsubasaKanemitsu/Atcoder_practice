s = list(input())

ans = []

for ss in s:
    if ss == '0':
        ans.append('0')
    elif ss == '1':
        ans.append('1')
    elif ss == '6':
        ans.append('9')
    elif ss == '8':
        ans.append('8')
    else:
        ans.append('6')
print(''.join(ans[::-1]))
