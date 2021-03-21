n = int(input())

contest = 'ABC'

if n >= 1000:
    contest = 'ABD'
    n -= 999

n = str(n).zfill(3)

print(contest)