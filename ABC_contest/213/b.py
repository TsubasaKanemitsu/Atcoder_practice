n = int(input())
A = list(map(int, input().split()))

num = []
for idx, a in enumerate(A):
    num.append((idx + 1, a))
num.sort(key=lambda x:x[1], reverse=True)

print(num[1][0])