n, k = list(map(int, input().split()))
A = list(map(int, input().split()))
A = list(map(lambda x: x - 1, A))

arrive_time = [0] * n
flag = [False] * n
st = 0
time = 0
while flag[st] == False:
    arrive_time[st] = time
    flag[st] = True
    time += 1
    st = A[st]
    if time == k:
        print(st + 1)
        exit()

k = (k - arrive_time[st]) % (time - arrive_time[st])
for i in range(k):
    st = A[st]
print(st + 1)
