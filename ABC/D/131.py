n = int(input())
work = []
a = []
b = []

for i in range(n):
    _a, _b = list(map(int, input().split()))
    work.append([_a, _b])
    
work = sorted(work, key=lambda x: x[1])

time = 0
for i in range(len(work)):
    time += work[i][0]
    if time > work[i][1]:
        print("No")
        exit()
print("Yes")