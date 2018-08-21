
if __name__ == '__main__':
    print("1부터 n까지의 합을 구합니다.")
    n = int(input("n의 값 : "))
    sum = 0
    i = 1

    while i <= n:
        sum += i
        i += 1

    print("1부터 {}까지의 합은 {} 입니다.".format(n, sum))

