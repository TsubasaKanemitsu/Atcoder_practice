S = input()
T = input()

result = "No"
for i in range(len(S)):
    word = S[i + 1:] + S[0:i + 1]
    if word == T:
        result = "Yes"
        break
print(result)