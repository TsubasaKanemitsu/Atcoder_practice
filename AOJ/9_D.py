word = list(input())
exec_num = int(input())
result = []
for i in range(0, exec_num):
    exec_command = list(input().split())
    a = int(exec_command[1])
    b = int(exec_command[2])    
    if exec_command[0] == 'replace':
        word[a:b + 1] = exec_command[3] 
    elif exec_command[0] == 'reverse':
        word[a:b + 1] =  reversed(word[a: b + 1])
    elif exec_command[0] == 'print':
        result.append(word[a:b + 1])
        
for i in range(len(result)):
    print(''.join(result[i]))


# 11分