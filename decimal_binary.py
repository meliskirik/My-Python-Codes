def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return '0'

    binary_representation = ''
    while decimal_number:
        binary_representation = str(decimal_number % 2) + binary_representation
        decimal_number //= 2

    return binary_representation
decimal_number = int(input("Enter a decimal number: "))
binary_result = decimal_to_binary(decimal_number)
print(binary_result)


