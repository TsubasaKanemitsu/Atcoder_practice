x, y = list(map(int, input().split()))

ans = [x]
count = 1
while True:
    temp_ans = ans[count - 1] * 2
    if temp_ans <= y:
        ans.append(temp_ans)
    else:
        break
    count += 1
print(len(ans))