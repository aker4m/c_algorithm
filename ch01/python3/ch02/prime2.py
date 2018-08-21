N = 100000

if __name__ == '__main__':
    i = 0
    list_prime = []
    ptr = 0
    counter = 0
    list_prime.insert(ptr, 2)
    ptr += 1
    for n in range(3, N, 2):
        for i in range(1, ptr):
            counter += 1
            if n % list_prime[i] == 0:
                break
        if ptr == (i+1):
            list_prime.insert(ptr, n)
            ptr += 1
    for i in range(0, ptr):
        print("{} ".format(list_prime[i]), end='')
    print()
    print("나눗셈을 실행한 횟수 : {}".format(counter))
    print("{}까지의 소수의 갯수는 {} 입니다.".format(N, ptr))
