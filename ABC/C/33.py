s = input().split('+')

ans = 0
for formula in s:
    if len(formula) == 1:
        if int(formula) != 0:
            ans += 1
    else:
        formula = formula.replace('*', '')
        num = 1
        for f in list(formula):
            num *= int(f)
        if num != 0:
            ans += 1

print(ans)