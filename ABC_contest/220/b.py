k = int(input())
A, B = input().split()

ans = 1
a_ = 0
b_ = 0
for i, a in enumerate(A[::-1]):
    a_ += k ** i * int(a)
for i, b in enumerate(B[::-1]):
    b_ += k ** i * int(b)
print(a_ * b_)
