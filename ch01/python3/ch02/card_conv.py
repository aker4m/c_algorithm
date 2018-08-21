'''
no : 변환하는 정수
cd : 기수
cno : 변환한 값의 각 자리의 숫자를 저장하는 문자 배열
'''

def int_input(string):
    return int(input(string))

def card_convr(no, cd, cno):
    dchar = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = 0
    if no == 0:
        cno[digits] = dchar[0]
        digits += 1
    else:
        while no:
            cno.insert(digits, dchar[no % cd])
            digits += 1
            no = int(no / cd) 
    return cno

if __name__ == '__main__':
    retry = 1
    print("10진수를 기수 변환합니다.")
    while retry == 1:
        cno = []
        no = int_input("변환하는 음이 아닌 정수 : ")
        cd = int()
        while cd < 2 or cd > 36:
            cd = int_input("어떤 진수로 변환할까요?(2-36) : ")
        cno = card_convr(no, cd, cno)
        print("{}진수로는 ".format(cd), end='')
        for i in range(len(cno)-1, -1, -1):
            print("{}".format(cno[i]), end='')
        print(" 입니다.")
        retry = int_input("한 번 더 할까요?(1 - 예 / 0 - 아니오) : ")

