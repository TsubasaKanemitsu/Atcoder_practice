n, t = list(map(int, input().split()))

path = [list(map(int, input().split())) for _ in range(n)]
path = [p[0] for p in path if p[1] <= t]
if path == []:
    print("TLE")
    exit()
path.sort()
print(path[0])