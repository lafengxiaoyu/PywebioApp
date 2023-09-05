input_value = 6


def beautiful_decorator(func):
    def do_something(x, y):
        return func(x ** 2, x // y + x % y)
    return do_something


@beautiful_decorator
def add_two_numbers(a, b):
    return a - b


c = add_two_numbers(3, input_value)
print("output is: ", c)