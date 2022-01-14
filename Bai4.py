chuoi = ', '
thongtin = input("Nhập vào chuỗi tên và mã sinh viên: ")
giatri = chuoi.join(thongtin)
danhsach=giatri.split(",")
tuple=tuple(danhsach)
print ("Danh sách là: ",danhsach, end=" ")
print("")
print ("Tuple là: ",tuple, end=" ")