n = int(input())
T = list(map(int, input().split()))
m = int(input())
PX = [list(map(int, input().split())) for _ in range(m)]

t_time = sum(T)

for i in range(m):
    p_num, x = PX[i]
    p_num -= 1
    t = T[p_num]
    diff = t - x
    print(t_time - diff)