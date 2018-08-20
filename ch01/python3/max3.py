def int_input(string):
    return int(input(string))

if __name__ == '__main__':
    print("세 정수의 최댓값을 구합니다.")
    a = int_input("a의 값 : ")
    b = int_input("b의 값 : ")
    c = int_input("c의 값 : ")
    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    print("최댓값은 {} 입니다.".format(max))
