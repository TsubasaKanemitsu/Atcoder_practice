a, v = list(map(int, input().split()))
b, w = list(map(int, input().split()))
t = int(input())

ab = abs(a - b)
wv = v - w

if ab <= wv * t:
    print("YES")
else:
    print("NO")