n = int(input())

a = list(map(int, input().split()))

unique_a = list(set(a))

sum_a = sum(a)
sum_unique_a = sum(unique_a)

if sum_a == sum_unique_a:
    print("YES")
else:
    print("NO")