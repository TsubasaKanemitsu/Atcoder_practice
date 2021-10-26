n = int(input())
AB = [list(map(int, input().split())) for _ in range(n)]

C = []
for a, b in AB:
    C.append(a / b)
sm_c = sum(C)
left_idx = 0
right_idx = n - 1
left_time = 0


cum_sm = 0
for i in range(len(C)):
    left_time += C[i]
    if left_time > sm_c / 2:
        left_idx = i
        break
time = sum(C[0:left_idx])
# print(time, left_idx)
diff = (sm_c / 2) - time
dist = 0
for i in range(left_idx):
    dist += AB[i][0]

print(dist + diff * AB[left_idx][1])
