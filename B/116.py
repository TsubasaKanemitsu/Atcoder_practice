s = int(input())

ai = [s]
count = 1
if s % 2 == 0:
    ai.append(s // 2)
else:
    ai.append(3 * s + 1)
i = 1

result = "continue"
while result == "continue":
    ai_1 = ai[i]
    if ai_1 % 2 == 0:
        ai.append(ai_1 // 2)
    else:
        ai.append(3 * ai_1 + 1)
    i += 1
    for j in range(len(ai)):
        for k in range(j + 1, len(ai)):
            if ai[j] == ai[k]:
                print(k + 1)
                result = "end"
                break
