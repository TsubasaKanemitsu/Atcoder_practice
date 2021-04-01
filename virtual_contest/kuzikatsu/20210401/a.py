import datetime

m1, d1 = list(map(int, input().split()))
m2, d2 = list(map(int, input().split()))

dt1 = datetime.datetime(2019, m1, d1)
dt2 = dt1 + datetime.timedelta(days=1)

if dt2.month == m1 + 1:
    print(1)
else:
    print(0)