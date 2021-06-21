n, a, b = list(map(int, input().split()))
S = input()

ok = 0
oversea = 0

for i in range(n):
    if S[i] == 'a' and ok < a + b:
        ok += 1
        print("Yes")
    elif S[i] == 'b' and ok < a + b and oversea < b:
        ok += 1
        oversea += 1
        print("Yes")
    else:
        print("No")