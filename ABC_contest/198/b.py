n = input()
nn = len(n)

st = 0
for i in range(len(n)):
    if n[i] == '0':
        while n[i] == '0' and (i + 1) < len(n):
            i += 1
        st = i
        break
    else:
        break

end = int(n)
for i in range(len(n) - 1, -1, -1):
    if n[i] != '0':
        end = i
        break

# print(st, end, nn)

if st == end:
    st = 0

new_n = n[st:end + 1]
rev_n = new_n[::-1]

# print(new_n, rev_n, nn)
if st <= (nn - (end + 1)) and new_n == rev_n:
    print("Yes")
else:
    print("No")