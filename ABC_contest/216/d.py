# from collections import defaultdict, deque
# n, m = list(map(int, input().split()))

# Q = deque()

# A = []
# # どの棒に所属しているか
# for i in range(m):
#     k = int(input())
#     a = list(map(int, input().split()))
#     temp = deque()
#     for j in range(k):
#         temp.push(a[j])
#     A.append(temp)

# available = [-1] * n


# def setAvailable(i):

#     if len(A[i]) == 0:
#         return

#     if 0 <= available[A[i].popleft()]:
#         # 現在の先頭の値と筒の番号を挿入
#         Q.push(available[A[i].popleft()], i)
#     else:
#         available[A[i].popleft()] = i


# for i in range(m):
#     setAvailable(i)

# while len(Q) > 0:
