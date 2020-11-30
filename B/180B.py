import math
N = int(input())

x = list(map(int, input().split()))

m_dis = sum(list(map(lambda x: abs(x), x)))

u_dis = sum(list(map(lambda x: abs(x) ** 2, x)))
u_dis = math.sqrt(u_dis)

ch_dis = max(list(map(lambda x: abs(x), x)))

print(m_dis)
print(u_dis)
print(ch_dis)