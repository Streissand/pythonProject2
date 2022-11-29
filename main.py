class ageCal:
    nameList = []
    ageList = []
    numberofAges = 0

    def __init__(self):
        pass

    def readData(self):
        file = open("ages.txt", mode='r', encoding='utf-8')
        data = file.readlines()
        print("data",data)

        for item in data:
            list1 = item.rstrip("\n")
            list2 = list1.split(",")
            self.nameList.append(list2[0])
            self.ageList.append(int(list2[1]))
            file.close()

        print("nameList:", self.nameList)
        print("ageList:", self.ageList)

        userinput = input("Enter a new age:")
        while userinput.isnumeric() == False:
            userinput = input("Enter a new age:")

        self.ageList.append(int(userinput))
        print("Updates ageList", self.ageList)

        self.numberofAges = len(self.ageList)

    def averageAge(self):
        totalAge = 0
        for item in self.ageList:
            totalAge = totalAge + item
        return totalAge/self.numberofAges

classInstance = ageCal()
classInstance.readData()
print("Average Age is:", classInstance.averageAge(), "No of ages is:", classInstance.numberofAges)