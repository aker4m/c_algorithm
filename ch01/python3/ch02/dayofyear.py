def int_input(string):
    return int(input(string))

mdays = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]]

def isleap(year):
    return int(year % 4 == 0 and year % 100 != 0 or year % 400 == 0)

def dayofyear(year, month, day):
    days = day
    for i in range(1, month):
        days += mdays[isleap(year)][i-1]
    return days

if __name__ == '__main__':
    retry = 1
    while retry == 1:
        year = int_input("년 : ")
        month = int_input("월 : ")
        day = int_input("일 : ")
        print("{}년의 {}일째 입니다.".format(year, dayofyear(year, month, day)))
        retry = int_input("다시 할까요?(1 - 예 / 0 - 아니오) : ")
