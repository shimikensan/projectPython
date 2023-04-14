import init as ok
class funtionsSV:
    listSV = []
    def generID(self):
        id = len(self.listSV) + 1
        return id
    def inputInfo(self):
        id = self.generID()
        name = input("Nhập tên sinh viên: ")
        age = int(input("Nhập tuổi sinh viên: "))
        addr = input("Nhập địa chỉ sinh viên: ")
        sv = ok.quanlySV(id, name, age, addr)
        self.listSV.append(sv)
    def delSV(self):
        nameSV = input("Nhập họ tên sinh viên.")
        for sv in self.getlistSV():
            if nameSV == sv.name:
                self.getlistSV().remove(sv)
    def updateSV(self):
        nameSV = input("Nhập họ tên sinh viên cần sửa: ")
        for sv in self.getlistSV():
            if nameSV == sv.name:
                sv.name = input("Nhập tên sinh viên mới: ")
                sv.age = int(input("Nhập tuổi sinh viên mới: "))
                sv.addr = input("Nhập địa chỉ sinh viên mới: ")
    def showInfo(self):
        print("THÔNG TIN SINH VIÊN")
        print("{:^75}".format("-"*75))
        print("|{:^10}|{:^30}|{:^10}|{:^20}|".format("ID", "Tên SV", "Tuổi SV", "Địa chỉ"))
        print("{:^75}".format("-"*75))
        for sv in self.getlistSV():
            print("|{:^10}|{:^30}|{:^10}|{:^20}|".format(sv.id, sv.name, sv.age, sv.addr))
            print("{:^75}".format("-"*75))
    def sortbyName(self):
        self.getlistSV().sort(key=lambda x: x.name)
        print("{:^75}".format("-"*75))
        print("|{:^10}|{:^30}|{:^10}|{:^20}|".format("ID", "Tên SV", "Tuổi SV", "Địa chỉ"))
        print("{:^75}".format("-"*75))
        for sv in self.getlistSV():
            print("|{:^10}|{:^30}|{:^10}|{:^20}|".format(sv.id, sv.name, sv.age, sv.addr))
            print("{:^75}".format("-"*75)) 
    def sortbyAge(self):
        self.getlistSV().sort(key=lambda x: x.age)
        print("{:^75}".format("-"*75))
        print("|{:^10}|{:^30}|{:^10}|{:^20}|".format("ID", "Tên SV", "Tuổi SV", "Địa chỉ"))
        print("{:^75}".format("-"*75))
        for sv in self.getlistSV():
            print("|{:^10}|{:^30}|{:^10}|{:^20}|".format(sv.id, sv.name, sv.age, sv.addr))
            print("{:^75}".format("-"*75))
    def sortbyaddr(self):
        self.getlistSV().sort(key=lambda x : x.addr)
        print("{:^75}".format("-"*75))
        print("|{:^10}|{:^30}|{:^10}|{:^20}|".format("ID", "Tên SV", "Tuổi SV", "Địa chỉ"))
        print("{:^75}".format("-"*75))
        for sv in self.getlistSV():
            print("|{:^10}|{:^30}|{:^10}|{:^20}|".format(sv.id, sv.name, sv.age, sv.addr))
            print("{:^75}".format("-"*75))             
    def getlistSV(self):
        return self.listSV
    def filtByName(self):
        inputSV = input("Nhập tên sinh viên: ")
        print("{:^75}".format("-"*75))
        print("|{:^10}|{:^30}|{:^10}|{:^20}|".format("ID", "Tên SV", "Tuổi SV", "Địa chỉ"))
        print("{:^75}".format("-"*75))
        for sv in self.getlistSV():
            if inputSV == sv.name:
                print("|{:^10}|{:^30}|{:^10}|{:^20}|".format(sv.id, sv.name, sv.age, sv.addr))
                print("{:^75}".format("-"*75))
    def filtByAge(self):
        inputSV = input("Nhập tên sinh viên: ")
        print("{:^75}".format("-"*75))
        print("|{:^10}|{:^30}|{:^10}|{:^20}|".format("ID", "Tên SV", "Tuổi SV", "Địa chỉ"))
        print("{:^75}".format("-"*75))
        for sv in self.getlistSV():
            if inputSV == sv.age:
                print("|{:^10}|{:^30}|{:^10}|{:^20}|".format(sv.id, sv.name, sv.age, sv.addr))
                print("{:^75}".format("-"*75))
    def filtByAddr(self):
        inputSV = input("Nhập tên sinh viên: ")
        print("{:^75}".format("-"*75))
        print("|{:^10}|{:^30}|{:^10}|{:^20}|".format("ID", "Tên SV", "Tuổi SV", "Địa chỉ"))
        print("{:^75}".format("-"*75))
        for sv in self.getlistSV():
            if inputSV == sv.addr:
                print("|{:^10}|{:^30}|{:^10}|{:^20}|".format(sv.id, sv.name, sv.age, sv.addr))
                print("{:^75}".format("-"*75))






