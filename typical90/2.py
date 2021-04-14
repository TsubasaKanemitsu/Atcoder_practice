# 20分
# bit全探索
n = int(input())


data = []
for bit in range(1 << n):
    word = ''
    left = 0
    right = 0
    for i in range(n):
        if bit & 1 << i:
            word += '('
            left += 1
        else:
            word += ')'
            right += 1
        if right > left:
            break

    if left == right:
        data.append(word)    

data.sort()
for i in range(len(data)):
    print(data[i])