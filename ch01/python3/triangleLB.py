def int_input(string):
    return int(input(string))

if __name__ == '__main__':
    n = int_input("몇 단 삼각형입니까? : ")
    while n <= 0:
        n = int_input("몇 단 삼각형입니까? : ")

    for i in range(1, n+1):
        for j in range(1, i+1):
            print('*', end='')
        print()
