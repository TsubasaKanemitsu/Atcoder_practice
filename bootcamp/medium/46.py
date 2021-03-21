# 43分
s = input()

if len(s) == 1:
    print("YES")
    exit()

a_count = s.count('a')
b_count = s.count('b')
c_count = s.count('c')

data = [[a_count, 'a'], [b_count, 'b'], [c_count, 'c']]
data.sort(reverse=True)
# print(data)

word = ''

while data[0][0] > 0 or data[1][0] > 0 or data[2][0] > 0:
    if data[0][0] > 0:
        word += data[0][1]
        data[0][0] -= 1
    if data[1][0] > 0:
        word += data[1][1]
        data[1][0] -= 1
    if data[2][0] > 0:
        word += data[2][1]
        data[2][0] -= 1
    
# print(word)
# 隣同士同じか?
for i in range(1, len(word)):
    if word[i - 1] == word[i]:
        print("NO")
        exit()

for i in range(1, len(word) - 1):
    if word[i - 1] == word[i + 1]:
        print("NO")
        exit()
print("YES")