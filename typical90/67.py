import sys
sys.setrecursionlimit(10 ** 7)

N, K = input().split()

def Base_10_to_n(X, N):
    if (int(X / N)):
        return Base_10_to_n(int(X / N), N) + str(X % N)
    return str(X % N)

oct = [int(c) for c in N[::-1]]

for i in range(int(K)):
    dec = sum([o * 8 ** i for i, o in enumerate(oct)])
    nine = Base_10_to_n(dec, 9)
    oct = str(nine).replace('8', '5')
    oct = list(map(int, list(oct)))
    oct = oct[::-1]

print(*oct[::-1], sep="")
