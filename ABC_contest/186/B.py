h, w = list(map(int, input().split()))

a = []
for i in range(h):
    a.extend(list(map(int, input().split())))

min_a = min(a)

new_a = [i for i in a if i != min_a]

sum_diff = 0
for num in new_a:
    sum_diff += num - min_a

print(sum_diff)