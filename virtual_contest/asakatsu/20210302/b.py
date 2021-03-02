n = int(input())
a, b = list(map(int, input().split()))
k = int(input())
p = list(map(int, input().split()))

if p.count(a) == 0 and p.count(b) == 0 and len(p) == len(set(p)):
    print("YES")
else:
    print("NO")
