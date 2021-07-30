# ABC156 C
# 4分半
# 全探索

n = int(input())
x = list(map(int, input().split()))
hp = 10 ** 99
for p in range(1, 101):
    temp_hp = 0
    for i in range(n):
        temp_hp += (x[i] - p) ** 2
    hp = min(hp, temp_hp)
print(hp)