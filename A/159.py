n, m = list(map(int, input().split()))

n_result = int(n * (n - 1) / 2)
m_result = int(m * (m - 1) / 2)
print(m_result + n_result)

