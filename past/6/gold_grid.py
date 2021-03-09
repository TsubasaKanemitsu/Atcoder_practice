from collections import deque, defaultdict
n, X, Y = list(map(int, input().split()))
grid = defaultdict(lambda: '.')

def construct_grid():
    for _ in range(n):
        ox, oy = map(int, input().split())
        grid[(ox, oy)] = '#'

    for i in range(- 202, 202 + 1):
        grid[(202, i)] = '#'
        grid[(-202, i)] = '#'
        grid[(i, 202)] = '#'
        grid[(i, -202)] = '#'

    grid[(X, Y)] = 'G'

move = ((1, 1), (0, 1), (- 1, 1), (1, 0), (- 1, 0), (0, -1))

def BFS():
    Q = deque()
    Q.append((0, 0, 0))
    grid[(0, 0)] = '!'

    while len(Q) > 0:
        x, y, move_count = Q.popleft()
        for dx, dy in move:
            xx = x + dx
            yy = y + dy
            
            if grid[(xx, yy)] == '.':
                Q.append((xx, yy, move_count + 1))
                grid[(xx, yy)] = '!'
            elif grid[(xx, yy)] == 'G':
                
                return move_count + 1
    return -1


construct_grid()

print(BFS())
