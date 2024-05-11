# bi listem var listedeki tüm elemanları topla ama ilk cift sayı haric
def sum_not_first_even(list):
    counter = 0
    total = 0
    for each_number in list:
        if each_number % 2 == 0 and counter == 0:
            list.remove(each_number)
            counter += 1
    for i in list:
        total += i
    return total
print(sum_not_first_even([1, 2, 3, 4, 5 ]))



