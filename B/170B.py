X, Y = list(map(int, input().split()))
result = "No"
for kame in range(X + 1):
    turu = X - kame
    animal = kame + turu
    foot = 2 * turu + 4 * kame
    if animal == X and foot == Y:
        result = "Yes"
print(result)