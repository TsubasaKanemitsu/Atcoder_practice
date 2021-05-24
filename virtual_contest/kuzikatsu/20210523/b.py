S = list(input())
n = len(S)
if S[0:(n - 1)//2] == S[(n + 3)//2 - 1:]:
    print("Yes")
else:
    print("No")