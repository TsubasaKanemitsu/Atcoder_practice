n, a, b = list(map(int, input().split()))
s = input()

pass_person = 0
b_cnt = 0

ans = []
for i in range(n):
    if s[i] == 'a' and pass_person < a + b:
        pass_person += 1
        ans.append("Yes")
    
    elif s[i] == 'b' and pass_person < a + b and b_cnt < b:
        pass_person += 1
        b_cnt += 1
        ans.append("Yes")
    else:
        ans.append("No")
    
for a in ans:
    print(a)