N = int(input())
input_data_list = []
for _ in range(N):
    input_data_list.append(int(input()))
input_data_list = list(set(input_data_list))

result = len(input_data_list)
print(result)