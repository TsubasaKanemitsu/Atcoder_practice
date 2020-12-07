while True:
    n = int(input())
    if n == 0:
        break
    else:
        num_list = list(map(float, input().split()))
        sm = 0
        var = 0
        for i in range(n):
            sm += num_list[i]
        mean = sm / n
        for i in range(n):
            var += (num_list[i] - mean) ** 2
        var = var / n
        std = var ** 0.5
    print(std)