a, b, x = list(map(int, input().split()))

def is_ok(m, target):
    if a * m + b * len(str(m)) <= target:
        return True
    else:
        False

def binary_search(target):
    left = 0
    right = 10 ** 9 + 1
    
    while right - left > 1:
        mid = left + (right - left) // 2
        if is_ok(mid, x):
            left = mid
        else:
            right = mid
    return left

ans = binary_search(x)

print(ans)

