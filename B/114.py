s = input()

val = 0
diff = 753
ans = 0
for i in range(len(s) - 2):
    val = int(s[i:i + 3])
    temp_diff = abs(753 - val)
    diff = min(temp_diff, diff)
print(diff)