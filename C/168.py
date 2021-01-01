import math
a, b, h, m = list(map(int, input().split()))

m = h * 60 + m

a_theta = 0.5 * m 
b_theta = 6.0 * m 
theta_diff = abs(a_theta - b_theta)

ans = a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(theta_diff))
print(ans ** 0.5)