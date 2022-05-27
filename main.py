from abc import ABC


class Count(ABC):
    def __init__(self, address):
        self.address = address

    def calculateFreqs(self):
        pass


class ListCount(Count):
    def __init__(self, address):
        Count.__init__(self, address)

    def calculateFreqs(self, address):
        f = open(address)
        x = f.readline().split()
        x2 = []
        for i in x:
            if i not in x2:
                x2.append(i)
        for i in range(0, len(x2)):
            print("Frequency of", x2[i], "is:", x.count(x2[i]))


class DictCount(Count):
    def __init__(self, address):
        Count.__init__(self, address)

    def calculateFreqs(self, address):
        f = open(address)
        x = f.readline()
        my_dict = {}
        for i in x.split():
            my_dict[i] = my_dict.get(i, 0) + 1
        for key in my_dict:
            print("{}: {}".format(key, my_dict[key]))


file = "strange.txt"

f1 = ListCount(file)
f1.calculateFreqs(file)

f2 = DictCount(file)
f2.calculateFreqs(file)
