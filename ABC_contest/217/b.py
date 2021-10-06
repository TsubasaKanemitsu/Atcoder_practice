s = {input() for _ in range(3)}
ans = {"ABC", "ARC", "AGC", "AHC"}

ans = ans - s
print(list(ans)[0])