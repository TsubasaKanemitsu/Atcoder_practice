def get_new_val(x, y):
    return (x + y) / 2

n = int(input())
v = sorted(list(map(int, input().split())))
result = v[0]
i = 1
while True:
    result = get_new_val(result, v[i])
    i += 1
    if i == n:
        break
print(result)

# 足して割る2を何度もするので，大きい値ほど最後の方で計算するのが望ましい
# そのため，ソートを昇順で行うことで実現可能
