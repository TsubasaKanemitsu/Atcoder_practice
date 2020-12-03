flag = 1
M = []
F = []
R = []
while flag > 0:
    m, f, r  = list(map(int, input().split()))
    if m == -1 and f == -1 and r == -1:
        flag = -1
    else:
        M.append(m)
        F.append(f)
        R.append(r)


for i in range(len(M)):
    if M[i] == -1 or F[i] == -1:
        print('F')
    else:
        test_score = M[i] + F[i]
        if test_score >= 80:
            print('A')
        elif 65 <= test_score < 80:
            print('B')
        elif 50 <= test_score < 65:
            print('C')
        elif 30 <= test_score < 50:
            if R[i] >= 50:
                print('C')
            else:
                print('D')
        else:
            print('F')
