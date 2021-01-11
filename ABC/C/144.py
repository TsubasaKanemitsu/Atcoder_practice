n = int(input())

def get_max_div_mod(n):
    itr = 1
    result = [1, 1]
    while itr * itr <= n:
        if n % itr == 0:
            result = [itr, n // itr]
        itr += 1
       
    return result

result = get_max_div_mod(n)

print(sum(result) - 2)            