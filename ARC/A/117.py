# 13分
A, B = list(map(int, input().split()))

if A == B:
    a_num = [i for i in range(1, A + 1)]
    b_num = [-i for i in range(1, B + 1)]
    ans = []
    ans.extend(a_num)
    ans.extend(b_num)
    ans = map(str, ans)
    print(' '.join(ans))
elif A > B:
    a_num = [i for i in range(1, A + 1)]
    b_num = [-i for i in range(1, B)]
    b_num.append(- (sum(a_num) + sum(b_num)))
    ans = []
    ans.extend(a_num)
    ans.extend(b_num)
    ans = map(str, ans)
    print(' '.join(ans))
else:
    a_num = [i for i in range(1, A)]
    b_num = [-i for i in range(1, B + 1)]
    a_num.append(- (sum(a_num) + sum(b_num)))
    ans = []
    ans.extend(a_num)
    ans.extend(b_num)
    ans = map(str, ans)
    print(' '.join(ans))