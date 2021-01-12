w = list(input())

word = set(w)

for wd in word:
    if w.count(wd) % 2 != 0:
        print("No")
        exit()
print("Yes")