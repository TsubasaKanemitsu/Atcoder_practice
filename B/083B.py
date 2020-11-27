input_data_list = list(map(int, input().split()))

number_list = []
cum_sum = 0
sub_cum_sum = 0
for i in range(1, input_data_list[0] + 1):
    j = i
    while j > 0:
        sub_cum_sum += int(j % 10)
        j = int(j / 10)
    if sub_cum_sum >= input_data_list[1] and sub_cum_sum <= input_data_list[2]:
        cum_sum += i
    sub_cum_sum = 0
print(cum_sum)
