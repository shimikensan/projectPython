import quanlysinhvien as okmen
import os
os.system("cls")
qlSV = okmen.funtionsSV()
while True:
    def showMenu():
        os.system("cls")
        print("PHẦN MỀN QUẢN LÝ SINH VIÊN")
        print("1. Nhập thông tin sinh viên.")
        print("2. Xem thông tin sinh viên.")
        print("3. Xoá Sinh viên.")
        print("4. Thay đổi thông tin sinh viên.")
        print("5. Sắp xếp.")
        print("6. Lọc dữ liệu.")
        print("0. Thoát")        
    showMenu()
    num = int(input("Chọn mục: "))
    if num == 1:
        os.system('cls')
        print("1. Nhập thông tin sinh viên:")
        qlSV.inputInfo()
        print("Bạn đã nhập xong.")
        num2 = int(input("Nhập 0 để trở lại."))
    if num == 2:
        os.system('cls')
        print("2. Xem thông tin sinh viên.")
        qlSV.showInfo()
    if num == 3:
        os.system('cls')
        print("3. Xoá sinh viên.")
        qlSV.delSV()
    if num == 4:
        os.system('cls')
        print('4. Thay đổi thông tin sinh viên')
        qlSV.updateSV()
        print('Đã thay đổi thành công')
    if num ==5:
        os.system("cls")
        print("5. Sắp xếp")
        print("a. Sắp xếp theo tên.")
        print("b. Sắp xếp theo tuổi.")
        print("c. Sắp xếp theo địa chỉ.")
        print("d. Exit.")
        num1 = input("Chọn đi bạn: ")
        if num1 == "a":
            print("Danh sách sinh viên sắp xếp theo tên")
            qlSV.sortbyName()
        if num1 == "b":
            print("Danh sách sắp xếp theo tuổi.")
            qlSV.sortbyAge()
        if num1 == "c":
            print("Danh sách sắp xếp theo địa chỉ.")
            qlSV.sortbyaddr()
        if num1 == "d":
            break
        else:
            print("Chọn lại đi bạn.")
    if num == 6:
        os.system("cls")
        print("5. Lọc thông tin học sinh.")
        print("a. Lọc theo tên.")
        print("b. Lọc theo tuổi.")
        print("c. Lọc theo địa chỉ.")
        print("d. Exit.")
        num1 = input("Chọn đi bạn: ")
        if num1 == "a":
            print("Danh sách sinh viên lọc theo tên")
            qlSV.filtByName()
        if num1 == "b":
            print("Danh sách lọc theo tuổi.")
            qlSV.filtByAge()
        if num1 == "c":
            print("Danh sách lọc theo địa chỉ.")
            qlSV.filtByAddr()
        if num1 == "d":
            break
        else:
            print("Chọn lại đi bạn.")
    if num == 0:
        break
    else:
        print("Vui lòng nhập lại.")