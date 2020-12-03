for i in range(1, 3001):
    input_data = list(map(int, input().split()))
    input_data.sort()
    if sum(input_data) == 0:
        break
    print(input_data[0], input_data[1])
