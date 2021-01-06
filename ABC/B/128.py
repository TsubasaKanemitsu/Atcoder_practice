N = int(input())

record = []
for i in range(N):
    S, P = input().split()
    P = int(P)
    record.extend([[i + 1, S, P]])

sorted_record = sorted(record, key=lambda x:(x[2]), reverse=True)
sorted_record = sorted(sorted_record, key=lambda x:(x[1]))

for i in range(N):
    print(sorted_record[i][0])
