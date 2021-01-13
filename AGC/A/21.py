N = input()
a = int(N)
N = list(N)
n = int(N[0])

chk = [0]*len(N)
for i in range(len(N)):
    chk[i] = int(N[i])

if sum(chk) != 9*len(N):
    if a < 10:
        print(n)
    elif n != 9 and sum(chk) == n + 9*(len(N)-1):
        print(sum(chk))
    else:
        print(n - 1 + (len(N) - 1)*9)
else:
    print(9*len(N)))
