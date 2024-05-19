def armstrong_finder():
    x = int(input("please enter a number between 1 to 9999: "))
    a = x // 1000
    b = (x - a*1000 ) // 100
    c = (x - a*1000 - b*100 ) // 10
    d = (x - a*1000 - b*100 - c*10)

    if x in range(1,10000):
        if x == (a**3) + (b**3) + (c**3) + (d**3):
            print("this is armstrong number")
        else:
            print("this is not armstrong number")

    else:
        print("please enter a number between 1 to 9999")


armstrong_finder()

''' num = [int(x) for x in input("please enter a number betweeen 1 to 9999: ")]
size = len(num)

for i in num:
    print(i * 10**(size -i), end=".\n") '''