import math
n = int(input())

AB = [list(map(int, input().split())) for _ in range(n)]
CD = [list(map(int, input().split())) for _ in range(n)]

std_ab = AB[1]
std_cd = CD[2]
print("a", std_ab, std_cd)

def get_dist(x1, y1, x2, y2):
    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    return dist


def get_radian(x1, y1, x2, y2):
    radian = math.atan2(y2 - y1, x2 - x1)
    
    return radian


def get_degree(radian):
    degree = math.degrees(radian)
    
    return degree

ab = []
cd = []
for i in range(n):
    a, b = AB[i]
    c, d = CD[i]
    # 距離
    ab_dist = get_dist(a, b, std_ab[0], std_ab[1])
    cd_dist = get_dist(c, d, std_cd[0], std_cd[1])

    # 角度
    ab_degree = get_degree(get_radian(a, b, std_ab[0], std_ab[1]))
    cd_degree = get_degree(get_radian(c, d, std_cd[0], std_cd[1]))

    ab.append((ab_degree, ab_dist))
    cd.append((cd_degree, cd_dist))
print(ab)
print(cd)