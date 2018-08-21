N = 100

if __name__ == '__main__':
    cnt = 0
    counter = 0
    for n in range(2, N+1):
        i = 0
        for i in range(2, n+1):
            counter += 1
            if n % i == 0:
                break
        if n == i:
            print("{} ".format(n), end='')
            cnt += 1
    print()
    print("나눗셈을 실행한 횟수 : {}".format(counter))
    print("{}까지의 소수의 갯수는 {} 입니다.".format(N, cnt))
