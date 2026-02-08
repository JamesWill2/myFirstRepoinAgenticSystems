def check_even_odd(number):
    if number % 2 == 0:
        return "Number is Even"
    else:
        return "Number is Odd"


# function call
result = check_even_odd(10)
print(result)