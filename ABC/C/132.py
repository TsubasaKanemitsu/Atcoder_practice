k = int(input())

D = list(map(int, input().split()))
D.sort()
mid_num = D[k // 2]
mid_prev_num = D[k // 2 - 1]
num = [i for i in range(mid_prev_num + 1, mid_num + 1)]
print(len(num))