def beautiful_decorator(func):
    def do_something(x, y):
        return func(x ** 2, x // y + x % y)
    return do_something


@beautiful_decorator
def add_two_numbers(a, b):
    return a - b


def main():
    input_value = int(input("Enter your input number: "))
    sre = add_two_numbers(3, input_value)
    print("the result is: ", sre)


main()
