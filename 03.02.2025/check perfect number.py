def is_perfect_number(number):
    if number <= 0:
        return False
    divisor_sum = 0
     for i in range(1, number):
        if number % i == 0:
            divisor_sum += i
   
    return divisor_sum == number
input_number = 28
if is_perfect_number(input_number):
    print(input_number, "is a perfect number.")
else:
    print(input_number, "is not a perfect number.")
