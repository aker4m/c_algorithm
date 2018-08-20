def int_input(string):
    return int(input(string))

def med3(a, b, c):
    if a >= b:
        if b >= c:
            return b
        elif c >= a:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b

if __name__ == '__main__':
    print("세 정수의 중앙값을 구합니다.")
    a = int_input("a의 값 : ")
    b = int_input("b의 값 : ")
    c = int_input("c의 값 : ")

    print("중앙값은 {} 입니다.".format(med3(a, b, c)))
