first_num = int(input("birinci sayiniz: "))
second_num = int(input("ikinci sayiniz: "))
if first_num <= 0 or second_num <= 0:
    print("lutfen 0dan buyuk sayı giriniz")
else:
    if first_num < second_num:
        min_num = first_num
    else:
        min_num = second_num
    for i in range(min_num, 1, -1):
        if first_num % i == 0 and second_num % i == 0:
            print("bu sayilarin ebobu: ", i)
            break
    else:
        print("bu sayilarin ebobu", 1)


