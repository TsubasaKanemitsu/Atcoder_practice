n = int(input())
extract = []
def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)

for i in range(1, n + 1):
    ten = Base_10_to_n(i, 10)
    eight = Base_10_to_n(i, 8)
    if '7' in ten or '7' in eight:
        extract.append(i)

ans = n - len(extract)

print(ans)
    