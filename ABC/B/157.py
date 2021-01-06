matrix = []
for i in range(3):
    matrix.extend(list(map(int, input().split())))

N = int(input())
b = []
for i in range(N):
    b.append(int(input()))
for i in range(3 * 3):
    for j in range(N):
        if matrix[i] == b[j]:
            matrix[i] = 0
index_list = [i for i, x in enumerate(matrix) if x == 0]
if 0 in index_list and 1 in index_list and 2 in index_list:
    print("Yes")
elif 3 in index_list and 4 in index_list and 5 in index_list:
    print("Yes")
elif 6 in index_list and 7 in index_list and 8 in index_list:
    print("Yes")
elif 0 in index_list and 3 in index_list and 6 in index_list:
    print("Yes")
elif 1 in index_list and 4 in index_list and 7 in index_list:
    print("Yes")
elif 2 in index_list and 5 in index_list and 8 in index_list:
    print("Yes")
elif 0 in index_list and 4 in index_list and 8 in index_list:
    print("Yes")
elif 2 in index_list and 4 in index_list and 6 in index_list:
    print("Yes")
else:
    print("No")