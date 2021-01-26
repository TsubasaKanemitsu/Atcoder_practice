# 20分
# 復習必要
a = []

for i in range(3):
    a.extend(list(map(int, input().split())))

n = int(input())
b = [int(input()) for _ in range(n)]

index = []
for i in b:
    if i in a:
        index.append(a.index(i))

index = set(index)
if set([0, 1, 2]) <= index:
    print("Yes")
elif set([3, 4, 5]) <= index:
    print("Yes")
elif set([6, 7, 8]) <= index:
    print("Yes")
elif set([0, 4, 8]) <= index:
    print("Yes")
elif set([2, 4, 6]) <= index:
    print("Yes")
elif set([0, 3, 6]) <= index:
    print("Yes")
elif set([1, 4, 7]) <= index:
    print("Yes")
elif set([2, 5, 8]) <= index:
    print("Yes")
else:
    print("No")

# 考察
# aを一次元配列にした場合，何番が3つ揃えばビンゴになるのかをビンゴの全パターンに
# あてはめて，if分を記述し，条件に従うかを判定した．