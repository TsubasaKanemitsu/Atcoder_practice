# ABC 78 C
# 確率DP (復習)
# 解説: https://drken1215.hatenablog.com/entry/2019/03/23/175300
# 期待値漸化式, 回数の期待値

n, m = list(map(int, input().split()))
submit_time = 1900 * m + (n - m) * 100
ans = 2 ** m * submit_time
print(ans)