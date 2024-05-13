'''
def perfect_number(x):
    bolen = []
    total = 0
    for i in range(1,x):
        if x % i == 0:
            bolen.append(i)
            total += i
    if x == total:
        return True
    else:
        return False
print(perfect_number(27))
'''

def perfect_number_finder(y):
    perfectler = []
    for j in range(1, y):
        bolen = []
        total = 0
        for i in range(1, j):
            if j % i == 0:
                bolen.append(i)
                total += i
        if j == total:
            perfectler.append(j)

    return perfectler
result = perfect_number_finder(100)
print(result)


