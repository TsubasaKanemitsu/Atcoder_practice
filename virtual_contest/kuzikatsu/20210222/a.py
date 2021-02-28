import itertools
p, q, r = list(map(int, input().split()))
time = [p, q, r]
ans = 300
for comb in itertools.permutations(time, 2):
    temp_ans = comb[0] + comb[1]
    ans = min(ans, temp_ans)
print(ans)
