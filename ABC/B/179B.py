N = int(input())

continuous_counter = 0
result = "No"
for i in range(N):
    D_s, D_e = list(map(int, input().split()))
    if D_s == D_e:
        continuous_counter += 1
        if continuous_counter >= 3:
            result = "Yes"
    else:
        continuous_counter = 0

print(result)