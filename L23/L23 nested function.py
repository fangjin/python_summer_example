
def inner():
    for inner_number in [0, 1, 2]:
        print('    inner', inner_number)


def outer():
    for number in [0, 1, 2]:
        print("\nouter", number, "\n")
        inner()


outer()
