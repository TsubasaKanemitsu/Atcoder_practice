number = int(input())
arare_color = list(map(str, input().split()))

result = len(list(set(arare_color)))

if result == 3:
    print('Three')
else:
    print('Four')
