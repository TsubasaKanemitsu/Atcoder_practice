input_data_list = list(map(str, input().split()))
 
number_list = []
cum_sum = 0
for i in range(1, int(input_data_list[0])+1):
  # 総和算出用
  calc_data = i 
  # 各桁同士の総和計算用
  data = list(map(int, str(i)))
  result = sum(data)
  if result >= int(input_data_list[1]) and result <= int(input_data_list[2]):
  	cum_sum += calc_data
    
print(cum_sum)
