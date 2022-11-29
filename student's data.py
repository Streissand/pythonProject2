class calAvgHeight:
    names = []
    heights = []
    def totalstudentheight = 552
        pass
    def totalstudentcount = 3
        pass

    def __init__(self):
        pass

    def readdata(self):
        file = open("listOfStudentHeight.txt", mode='r', encoding='utf-8')
        data =file.readlines()
        print("data",data)

        for item in data:
            list1 = item.rstrip("\n")
            list2 = list1.split(",")
            self.names.append(list2[0])
            self.heights.append(int(list2[1]))
            file.close()

        print("names:", self.names)
        print("heights:", self.heights)

        userinput = input("Enter a new height:")
        while userinput.isnumeric() == False:
            userinput = input("Enter a new height:")

        self.heights.append(int(userinput))
        print("Updates heights", self.heights)

        self.totalstudentheight = len(self.heights)

    def averageheight(self):
        totalstudentheight = 0
        for item in self.heights:
            totalstudentheight = totalstudentheight + item
        return totalstudentcount/self.totalstudentheight

classInstance = totalstudentheight()
classInstance.readData()
print("Student average height is:", classInstance.averageheight)