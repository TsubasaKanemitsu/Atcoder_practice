from collections import deque
N = int(input())

# 最小にするために
# Aの最大と最小を取り続けて、行けばいいと思ったが
def solve(A: list, k):
    # O(k * n * n) == 10 ** 6
    if k == 0:
        return 0
    ans = 0
    A.sort()
    for _ in range(k):
        print(A)
        # 1回の交換でAの総和を最小にできる組み合わせを全探索する
        for i in range(len(A)):
            sum_ = sum(A)
            temp_sum = sum_
            pos = [0, 1]
            for j in range(len(A)):
                if i == j:
                    continue
                if A[j] == 0:
                    continue
                temp = sum_ - ((A[i] + A[j]) - A[i] // A[j])
                if temp_sum > temp:
                    temp_sum = temp
                    pos = [i, j]
                elif temp_sum == temp and A[i] + A[j] > A[pos[0]] + A[pos[1]]:
                    temp_sum = temp
                    pos = [i, j]
        print("pos", pos)
        x = A[pos[0]]
        y = A[pos[1]]
        temp_A = [A[i] for i in range(len(A)) if i != pos[0] and i != pos[1]]
        ans += x // y
        # temp_A.append(x // y)
        A = temp_A
        A.sort()

    return sum(A) + ans




    # return sum(list(A))


ans = []
for _ in range(N):
    n, k = list(map(int, input().split()))
    A = list(map(int, input().split()))
    ans.append(solve(A, k))

for a in ans:
    print(a)
    