num = int(input())
input_data_list = list(input().split())
input_data_list.reverse()
for i in range(num):
    print(input_data_list[i], end='')
    if i != num - 1:
        print(' ', end='')
print()