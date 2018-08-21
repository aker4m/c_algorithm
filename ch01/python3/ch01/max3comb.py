
def max3(a, b, c):
    max = a
    if b > max: max = b
    if c > max: max = c
    return max

def test_print(a, b, c):
    print("max3({}, {}, {}) = {}".format(a, b, c, max(a, b, c)))

if __name__ == '__main__':
    test_print(3, 2, 1)
    test_print(3, 2, 2)
    test_print(3, 1, 2)
    test_print(3, 2, 3)
    test_print(2, 1, 3)
    test_print(3, 3, 2)
    test_print(3, 3, 3)
    test_print(2, 2, 3)
    test_print(2, 3, 1)
    test_print(2, 3, 2)
    test_print(1, 3, 2)
    test_print(2, 3, 3)
    test_print(1, 2, 3)

