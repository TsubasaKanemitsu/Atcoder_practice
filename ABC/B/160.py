x = int(input())
five_hundreds = 0
five = 0

five_hundreds = x // 500
five = (x % 500) // 5

print(five_hundreds * 1000 + five * 5)
