def hello_world():
    print("Hello world!")

hello_world()

def sum(num1, num2=3):
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2


# sum(1, 2)
# sum(4, 90)
# sum(145, 432)

total = sum(7, 2)
print(total)

print(sum(3))


def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("Dave", "John", "Sarah")


def mult_named_items(**kwargs):   # keyword arguments
    print(kwargs)
    print(type(kwargs))

mult_named_items(first = "Loren", last = "Michael")
