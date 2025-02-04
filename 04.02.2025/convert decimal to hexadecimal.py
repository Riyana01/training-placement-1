def decimal_to_hexadecimal(n):
    return hex(n).replace("0x", "")

decimal_number = int(input("Enter a decimal number: "))
hexadecimal_number = decimal_to_hexadecimal(decimal_number)
print("Hexadecimal representation of", decimal_number, "is:", hexadecimal_number)
