def int_input(string):
    return int(input(string))

if __name__ == '__main__':
    print("1부터 n까지의 합을 구합니다.")
    n = int_input("n 값 : ")
    while n <= 0:
        n = int_input("n 값 : ")

    sum = 0
    for i in range(1, n+1):
        sum += i
    print("1부터 {}까지의 합은 {} 입니다.".format(n, sum))
