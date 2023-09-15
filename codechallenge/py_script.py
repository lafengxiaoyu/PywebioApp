def beautiful_decorator(func):
    def trick_you(x, y):
        return func(x ** 2, x % y)
    return trick_you


@beautiful_decorator
def add_two_numbers(a, b):
    return a - b


def py_script():
    input_value = int(input("Enter your input number: "))
    sre = add_two_numbers(3, input_value)
    print("the result is: ", sre)


# run the script
py_script()
