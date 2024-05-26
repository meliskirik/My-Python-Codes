def power_num(x,n):
    if n == 0:
        return 1
    else:
        return x * power_num(x,n-1)
print(power_num(3,2))