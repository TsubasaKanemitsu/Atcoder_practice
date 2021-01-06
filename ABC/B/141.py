s = input()
l = len(s)

odd = [s[i] for i in range(0, len(s), 2)]
gu = [s[i] for i in range(1, len(s), 2)]

_gu = set(['L', 'U', 'D'])
_odd = set(['R', 'U', 'D'])

ans_gu = len(list(set(gu) - _gu))
ans_odd = len(list(set(odd) - _odd))
if ans_gu == 0 and ans_odd == 0:
    print("Yes")
else:
    print("No")

