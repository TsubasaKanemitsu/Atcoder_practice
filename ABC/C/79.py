import itertools
num = list(map(int, input()))

for perm in itertools.product(['+', '-'], repeat=3):
    flag = False
    ans = num[0]
    str_ans = str(num[0])
    for index, p in enumerate(perm):
        if p == '+':
            ans += num[index + 1]
            str_ans += p + str(num[index + 1])
        else:
            ans -= num[index + 1]
            str_ans += p + str(num[index + 1])
    if ans == 7:
        print(f'{str_ans}={ans}')
        flag = True
        break
    if flag:
        break