n = int(input())
w = list(map(int, input().split()))

diff = n * 1000
for i in range(n):
    s1 = sum(w[0:i])
    s2 = sum(w[i:])
    diff = min(diff, abs(s1 - s2))
    
print(diff)