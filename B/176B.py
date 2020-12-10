N = list(map(int, input().split()))
ans = sum(N)
result = "No"

if ans % 9 == 0:
    result = "Yes"

print(result)
    
