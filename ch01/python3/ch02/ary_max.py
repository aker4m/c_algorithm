def int_input(string):
    return int(input(string))

def maxof(list_height, number):
    max = list_height[0]
    for i in range(1, number):
        if list_height[i] > max:
            max = list_height[i]
    return max

if __name__ == '__main__':
    number = int_input("사람 수 : ")
    height = []
    print("{} 사람의 키를 입력하세요.".format(number))
    for i in range(0, number):
        height.insert(i, int_input("height[{}] : ".format(i)))
    print("최댓값은 {} 입니다.".format(maxof(height, number)))

