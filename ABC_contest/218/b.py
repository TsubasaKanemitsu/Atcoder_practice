P = list(map(int, input().split()))

num = ord('a') - 1
for p in P:
    print(chr(num + p), end="")
