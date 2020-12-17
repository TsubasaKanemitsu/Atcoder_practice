s = list(input())
alpabet = [chr(ord('a') + i) for i in range(26)]

diff = list(set(alpabet) - set(s))

if len(diff) == 0:
    print("None")
else:
    diff = sorted(diff)
    print(diff[0])