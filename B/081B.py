N = int(input())
input_data_list = list(map(int, input().split()))
do_num = 0
while all([i % 2 == 0 for i in input_data_list]):
  do_num += 1
  input_data_list = [int(i /2) for i in input_data_list]
print(do_num)