def int_input(string):
    return int(input(string))

if __name__ == '__main__':
    print("2자리 정수를 입력하세요.")
    no = int_input("수는 : ")
    while no < 10 or no > 99:
        no = int_input("수는 : ")
    print("변수 no 값은 {}이 되었습니다.".format(no))
