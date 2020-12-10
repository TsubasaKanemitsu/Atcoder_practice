N = int(input())
input_data_list = list(map(int, input().split()))

input_data_list.sort(reverse=True)
Alice = sum(input_data_list[0::2])
Bob = sum(input_data_list[1::2])

result = Alice - Bob
print(result)