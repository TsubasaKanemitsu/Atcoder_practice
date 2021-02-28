n = int(input())

left = 1
right = n + 1

def binary_search(left, right, n):
    sum_val = (n * (n + 1)) // 2
    while right - left > 1:
        mid = left + (right - left) // 2
        # 区間和
        w_sum = (n * (n + 1)) // 2 - (mid * (mid + 1)) // 2
        num = w_sum + n + 1
        if num >= sum_val:
            left = mid
        else:
            right = mid
    return left

right = binary_search(left, right, n)
count = n + 1 - right
print(count)