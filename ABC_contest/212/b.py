X = list(map(int, list(input())))

if len(set(X)) == 1:
    print("Weak")
else:
    cnt = 0
    for i in range(len(X) - 1):
        if X[i + 1] == X[i] + 1 and 0 <= X[i] <= 8:
            cnt += 1
        elif X[i] == 9 and X[i + 1] == 0:
            cnt += 1

    if cnt != len(X) - 1:
        print("Strong")
    else:
        print("Weak")