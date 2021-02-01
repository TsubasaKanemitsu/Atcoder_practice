s = input()
s1 = int(s[0:2])
s2 = int(s[2:])


if 1 <= s1 <= 12 and 1 <= s2 <= 12:
    print("AMBIGUOUS")
elif 1 <= s2 <= 12:
    print("YYMM")
elif 1 <= s1 <= 12:
    print("MMYY")
else:
    print("NA")