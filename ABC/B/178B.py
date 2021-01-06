import numpy as np
a, b, c, d = list(map(int, input().split()))

result = max([a*c, a*d , b*c, b*d])
print(result)