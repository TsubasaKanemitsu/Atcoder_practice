t1, t2 = list(map(int, input().split()))
a1, a2 = list(map(int, input().split()))
b1, b2 = list(map(int, input().split()))

d_a1 = t1 * a1
d_a2 = t2 * a2
d_b1 = t1 * b1
d_b2 = t2 * b2

dist_a = d_a1 + d_a2
dist_b = d_b1 + d_b2

if dist_a == dist_b:
    print("infinity")
    exit()


print(dist_a, dist_b)


# print(abs(dist_a - dist_b) // b2)
# print(abs(a1 - b1))
# print(abs(d_a2 - d_b2))

print(d_b1 - d_a1)
print(dist_a - dist_b)

a = d_b1 - d_a1
b = dist_a - dist_b

print(a / b )