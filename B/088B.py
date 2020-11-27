N = int(input())
input_data_list = list(map(int, input().split()))
#Alice = []
#Bob = []
#while len(input_data_list) > 0:
#	max_val1 = max(input_data_list)
#	Alice.append(max(input_data_list))
#	input_data_list.remove(max_val1)
#	if len(input_data_list) == 0:
#		break
#	max_val2 = max(input_data_list)
#	Bob.append(max(input_data_list))
#	input_data_list.remove(max_val2)
#Alice_val = sum(Alice)
#Bob_val = sum(Bob)
	
#result = Alice_val - Bob_val

#print(result)

input_data_list.sort(reverse=True)
Alice = sum(input_data_list[0::2])
Bob = sum(input_data_list[1::2])

result = Alice - Bob
print(result)