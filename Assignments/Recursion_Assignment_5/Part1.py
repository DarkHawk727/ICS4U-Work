def recursive_divide(divident, divisor):
    if divident == 0:
        return 0
    elif divisor == 0:
        raise ZeroDivisionError
    if divident < divisor:
        return 0
    else:
        return 1 + recursive_divide(divident - divisor, divisor)


def recursive_remainder(divident, divisor):
    if divident < divisor:
        return divident
    else:
        return recursive_remainder(divident - divisor, divisor)


num1 = int(input("Please enter the divident: "))
num2 = int(input("Please enter the divisor: "))
print(
    "{} ÷ {} = {} with remainder {}".format(
        num1, num2, recursive_divide(num1, num2), recursive_remainder(num1, num2)
    )
)
