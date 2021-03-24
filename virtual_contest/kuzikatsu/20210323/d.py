k, t = list(map(int, input().split()))
a = list(map(int, input().split()))

a.sort(reverse=True)

top = a[0] - 1
zan_total = sum(a[1:])

diff = top - zan_total
if diff <= 0:
    diff = 0

print(diff)