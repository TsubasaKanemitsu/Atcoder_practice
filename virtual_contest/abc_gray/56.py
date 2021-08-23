# ABC 208 C
# 15 min
# 商と余り, sort

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

person = []

for i in range(n):
    person.append([i, a[i], 0])
    
person.sort(key=lambda x:x[1])

if k >= n:
    for i in range(n):
        j, aj, _ = person[i]
        person[i] = [j, aj, k // n]
        if i < k % n:
            person[i][2] += 1
else:
    for i in range(n):
        if i < k:
            j, aj, _ = person[i]
            person[i] = (j, aj, 1)

person.sort(key=lambda x:x[0])

for i in range(n):
    print(person[i][2])

            

