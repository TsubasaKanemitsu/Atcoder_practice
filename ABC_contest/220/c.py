# math.ceilのオーバーフロー
n = int(input())
A = list(map(int, input().split()))
X = int(input())

sm = sum(A)

# Xを超えないBになるまでに必要なAの総和の回数
num = X // sm

# X超えない状態での項数
ans = num * n

# Xを超えるのに必要な数
now = num * sm
for a in A:
    now += a
    ans += 1
    if now > X:
        break
print(ans)