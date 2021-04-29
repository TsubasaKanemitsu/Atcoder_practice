# 15分
# 制約：上向きになるサイコロの目は任意の目でいい
# xに以上にするために，サイコロの目として出てほしいのは
# 大きい目である．最初のサイコロの目を5にしておけば，一回目の移動で
# 6に移動することができ，さらに次の移動では5に移動することができる．
# この移動はサイコロの出る目の中で大きい目の上位2つなので
# この2つの目を交互に移動することで, x以上にするための操作回数を最小にすることができる．
# xを11(= 5 + 6)で割り，その余りが1 ~ 6の場合は，更に一度だけ6に移動する必要があり，
# 余りが7以上の場合は更に5に移動する必要がある．
# そのためxに到達する移動回数はxを11分割できる回数分×2 + 余り分の埋め合わせのために6 or (5 and 6)に移動する回数分を
# 足すことで求めることができる．

x = int(input())

mod = x % 11
if 1 <= mod <= 6:
    add = 1
elif 7 <= mod <= 10:
    add = 2
else:
    add = 0

ans = (x // 11) * 2 + add

print(ans)