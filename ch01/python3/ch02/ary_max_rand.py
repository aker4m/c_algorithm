import random

def maxof(list_height, number):
    max = list_height[0]
    for i in range(1, number):
        if list_height[i] > max:
            max = list_height[i]
    return max

def int_input(string):
    return int(input(string))

if __name__ == '__main__':
    list_height = []
    number = int_input("사람 수 : ")
    while number <= 0:
        number = int_input("사람 수 : ")
    for i in range(0, number):
        list_height.insert(i, 100 + random.randint(40, 90))
        print("height[{}] = {}".format(i, list_height[i]))
    print("최댓값은 {} 입니다.".format(maxof(list_height, number)))


