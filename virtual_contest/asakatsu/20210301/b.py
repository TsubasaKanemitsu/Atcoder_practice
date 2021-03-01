x = int(input())

price = [100, 101, 102, 103, 104, 105, 206, 207, 208, 209]

while x > 0:
    if str(x)[-1] == '0':
        x -= 100
    elif str(x)[-1] == '1':
        x -= 101
    elif str(x)[-1] == '2':
        x -= 102
    elif str(x)[-1] == '3':
        x -= 103
    elif str(x)[-1] == '4':
        x -= 104
    elif str(x)[-1] == '5':
        x -= 105
    elif str(x)[-1] == '6':
        x -= 206
    elif str(x)[-1] == '7':
        x -= 207
    elif str(x)[-1] == '8':
        x -= 208
    elif str(x)[-1] == '9':
        x -= 209
    print(x)
print(x)
if x == 0:
    print(1)
else:
    print(0)