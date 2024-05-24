def even(n):
    if n == 0:
        return True
    else:
        return not odd(n-1)
def odd(n):
    if n == 0:
        return False
    else:
        return not even(n-1)
print(even(5))