# S, N or W, Eのどちらか一方だけが0のとき家に戻れない
s = list(input())

s_cnt = s.count("S")
n_cnt = s.count("N")
w_cnt = s.count("W")
e_cnt = s.count("E")
if (s_cnt * n_cnt == 0 and s_cnt + n_cnt != 0) or (w_cnt * e_cnt == 0 and w_cnt + e_cnt != 0):
    print("No")
else:
    print("Yes")
