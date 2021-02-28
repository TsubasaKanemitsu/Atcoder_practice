n, k = list(map(int, input().split()))

A = list(map(int, input().split()))
A = [a - 1 for a in A]

# 到着回数
arrive_record = [-1] * n
st = 0
time = 0

# 2週目に入る前まで
while arrive_record[st] == -1:
    arrive_record[st] = time
    time += 1   
    st = A[st]
    if time == k:
        print(st + 1)
        exit()

# ループ開始からkまでの移動回数 % ループ周期
k = (k - arrive_record[st]) % (time - arrive_record[st])
for i in range(k):
    st = A[st]
print(st + 1)