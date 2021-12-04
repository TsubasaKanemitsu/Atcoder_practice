n = int(input())
AB = [list(map(int, input().split())) for _ in range(n)]

AB_ = [((- a - b), a, b) for a, b in AB]
AB_.sort()

ans = 0
for i in range(n):
    c, a, b = AB_[i]
    if i % 2 == 0:
        ans += a
    else:
        ans -= b

print(ans)


# sort条件をどのように見つけるのかが大切
# 複数の選択肢があり得るときに、
# その選び方で優先度をつけるのはどのような条件で
# つけるのかを考えるというのが着眼点の1つである