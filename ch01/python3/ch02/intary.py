NUMBER = 5

def int_input(string):
    return int(input(string))

if __name__ == '__main__':
    list_number = []
    for i in range(0, NUMBER):
        list_number.append(int_input("list_number[{}] : ".format(i)))
    print("각 요소의 값")
    for i in range(0, len(list_number)):
        print("list_number[{}] = {}".format(i, list_number[i]))

