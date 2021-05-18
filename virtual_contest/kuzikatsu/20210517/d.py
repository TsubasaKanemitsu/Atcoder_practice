from collections import deque
n, m, k = list(map(int, input().split()))
A = deque(map(int, input().split()))
B = deque(map(int, input().split()))

a_cnt = 0
b_cnt = 0
sum_time = 0
ans = 0
while True:
    if len(A) > 0 and len(B) > 0:
        if A[0] > B[0]:
            sum_time += B.popleft()
        elif A[0] < B[0]:
            sum_time += A.popleft()
        else:
            # 一番上の本が両方同じ時間掛かるとき
            if len(A) >= 2 and len(B) >= 2:
                if A[1] >= B[1]:
                    sum_time += B.popleft()
                elif A[1] < B[1]:
                    sum_time += A.popleft()
            else:
                if len(A) >= 2 and len(B) == 1:
                    sum_time += A.popleft()
                elif len(A) == 1 and len(B) >= 2:
                    sum_time += B.popleft()
                else:
                    sum_time += A.popleft()
                
    elif len(A) > 0 and len(B) == 0:
        sum_time += A.popleft()
        
    elif len(A) == 0 and len(B) > 0:
        sum_time += B.popleft()
        
    ans += 1

    if sum_time > k:
        ans -= 1
        break

    if len(A) == 0 and len(B) == 0:
        break
print(ans)