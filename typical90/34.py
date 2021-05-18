from collections import deque, defaultdict


n, k = list(map(int, input().split()))
A = list(map(int, input().split()))

cnt = defaultdict(int)
num = set()
Q = deque()

c = 0
ans = 0
for i in range(n):
    Q.append(A[i])
    # 現在，キューの中に入っている要素の個数をカウント
    cnt[A[i]] += 1
    # 一意な値の個数をカウント
    num.add(A[i])
    if len(num) > k:
        while len(num) > k:
            s = Q.popleft()
            # キューの左端から排出した数値をデクリメント
            cnt[s] -= 1
            # キューの中から該当の数値が消えたら一意な値を減らす
            if cnt[s] == 0:
                num.remove(s)
    c = len(Q)
    ans = max(ans, c)
print(ans)