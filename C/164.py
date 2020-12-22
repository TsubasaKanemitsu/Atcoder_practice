n = int(input())
s = []
for i in range(n):
    s.append(input())

l = len(list(set(s)))
print(l)