
VMAX = 21

class PhysCheck:
    def __init__(self, name, height, vision):
        self.name = name
        self.height = height
        self.vision = vision

def ave_height(list_class):
    sum = 0
    number = len(list_class)
    for i in range(0, number):
        sum += list_class[i].height
    return sum / number

def dist_vision(list_class, list_vdist):
    number = len(list_class)
    for i in range(0, VMAX):
        list_vdist.insert(i, 0)
    for i in range(0, number):
        if list_class[i].vision >= 0.0 and list_class[i].vision <= VMAX/10.0:
            list_vdist[int(list_class[i].vision * 10)] += 1
    return list_vdist

if __name__ == '__main__':
    list_class = [PhysCheck("박현규", 162, 0.3),
                    PhysCheck("함진아", 173, 0.7),
                    PhysCheck("최윤미", 175, 2.0),
                    PhysCheck("홍연의", 171, 1.5),
                    PhysCheck("이수진", 168, 0.4),
                    PhysCheck("김영준", 174, 1.2),
                    PhysCheck("박용규", 169, 0.8)]
    list_vdist = []
    print("-----신체검사표-----")
    print("이름  키 시력")
    print("-"*20)
    for i in range(0, len(list_class)):
        print("{} {} {}".format(list_class[i].name, 
                                list_class[i].height, 
                                list_class[i].vision))
    print()
    print("평균 키 : {:.2f} cm".format(ave_height(list_class)))
    list_vdist = dist_vision(list_class, list_vdist)
    print()
    print("시력 분포")
    for i in range(0, VMAX):
        print("{} ~ {}명".format(i/10.0, list_vdist[i]))


