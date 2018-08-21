N = 1000000

if __name__ == '__main__':
    list_prime = []
    ptr = 0
    counter = 0
    list_prime.insert(ptr, 2)
    ptr += 1
    list_prime.insert(ptr, 3)
    ptr += 1
    for n in range(5, N+1, 2):
        flag = 0
        max_index = 0
        for i in range(1, ptr):
            counter += 1
            if list_prime[i]**2 > n:
                max_index = i
                break
        for i in range(1, max_index+1):
            counter += 1
            if n % list_prime[i] == 0:
                flag = 1
                break
        if not flag:
            list_prime.insert(ptr, n)
            ptr += 1

    for i in range(0, ptr):
        print("{} ".format(list_prime[i]), end='')
    print()
    print("곱셈과 나눗셈을 실행한 횟수 : {}".format(counter))
    print("{}까지의 소수의 갯수는 {} 입니다.".format(N, ptr))
