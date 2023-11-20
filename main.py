class Student:
    def __init__(self, cccd, sbd, ho_ten, dia_chi):
        self._cccd = self._check_cccd(cccd)
        self._sbd = self._check_sbd(sbd)
        self._ho_ten = self._check_ho_ten(ho_ten)
        self._dia_chi = self._check_dia_chi(dia_chi)
    # get
    def get_cccd(self):
        return self._cccd
    def get_sbd(self):
        return self._sbd
    def get_ho_ten(self):
        return self._ho_ten
    def get_dia_chi(self):
        return self._dia_chi
    # set
    def set_cccd(self, cccd):
        self._cccd = self._check_cccd(cccd)
    def set_sbd(self, sbd):
        self._sbd = self._check_sbd(sbd)
    def set_ho_ten(self, ho_ten):
        self._ho_ten = self._check_ho_ten(ho_ten)
    def set_dia_chi(self, dia_chi):
        self._dia_chi = self._check_dia_chi(dia_chi)

    # check căn cước công dân
    def _check_cccd(self, cccd):
        # check độ dài vd cccd = 1
        if len(cccd) != 4:
            raise ValueError("Căn cước công dân phải có 12 ký tự")
        # check ký tự khác số vd cccd = 123456789012a
        for i in cccd:
            if i.isdigit() == False:
                raise ValueError("Căn cước công dân phải là số")
        # check rỗng vd cccd = ""
        if cccd == "":
            raise ValueError("Căn cước công dân không được để trống")
        # check có phải số nguyên không vd cccd = 1.2
        if (int(cccd) == False):
            raise ValueError("Căn cước công dân phải là số nguyên")
        # check số âm vd cccd = -1
        if int(cccd) < 0:
            raise ValueError("Căn cước công dân không được là số âm")
        return cccd

    # check số báo danh
    def _check_sbd(self, sbd):
        # check rỗng
        if sbd == "":
            raise ValueError("Số báo danh không được để trống")
        return sbd

    # check họ tên
    def _check_ho_ten(self, ho_ten):
        # check rỗng
        if ho_ten == "":
            raise ValueError("Họ tên không được để trống")
        # check có phải là chữ không, tên có thể chứa khoảng trắng
        for i in ho_ten:
            if i.isdigit() == True:
                raise ValueError("Họ tên không được chứa số")
        return ho_ten

    # check địa chỉ
    def _check_dia_chi(self, dia_chi):
        # check rỗng
        if dia_chi == "":
            raise ValueError("Địa chỉ không được để trống")
        return dia_chi

    # get thông tin
    def get_info(self):
        print(f"CCCD: {self._cccd}, SBD: {self._sbd}, Họ tên: {self._ho_ten}, Địa chỉ: {self._dia_chi}")


class SinhVienA(Student):
    def __init__(self, cccd, sbd, ho_ten, dia_chi, toan, ly, hoa):
        super().__init__(cccd, sbd, ho_ten, dia_chi)
        self._toan = self._check_toan(toan)
        self._ly = self._check_ly(ly)
        self._hoa = self._check_hoa(hoa)
    # get
    def get_toan(self):
        return self._toan
    def get_ly(self):
        return self._ly
    def get_hoa(self):
        return self._hoa
    # set
    def set_toan(self, toan):
        self._toan = self._check_toan(toan)
    def set_ly(self, ly):
        self._ly = self._check_ly(ly)
    def set_hoa(self, hoa):
        self._hoa = self._check_hoa(hoa)

    # check điểm toán
    def _check_toan(self, toan):
        try:
            toan = float(toan)
            if toan < 0 or toan > 10:
                raise ValueError("Điểm toán không hợp lệ")
            return toan
        except ValueError:
            raise ValueError("Điểm toán phải là số thực")

    # check điểm lý
    def _check_ly(self, ly):
        try:
            ly = float(ly)
            if ly < 0 or ly > 10:
                 raise ValueError("Điểm lý không hợp lệ")
            return ly
        except ValueError:
            raise ValueError("Điểm lý phải là số thực")

# check điểm hóa
    def _check_hoa(self, hoa):
        try:
            hoa = float(hoa)
            if hoa < 0 or hoa > 10:
                raise ValueError("Điểm hóa không hợp lệ")
            return hoa
        except ValueError:
            raise ValueError("Điểm hóa phải là số thực")

    # get điểm trung bình
    def get_diem_tb(self):
        print(((self._toan + self._ly)+self._hoa) / 3)

    # get thông tin
    def get_info(self):
        print(
            f"CCCD: {self._cccd}, SBD: {self._sbd}, Họ tên: {self._ho_ten}, Địa chỉ: {self._dia_chi}, Điểm toán: {self._toan}, Điểm lý: {self._ly}, Điểm hóa: {self._hoa}")

    # get điểm:
    def get_tong_diem(self):
        return (self._toan * 1.5 + self._ly + self._hoa)

    # check liệt: môn nào điểm dưới 2 thì học sinh đó liệt
    def check_liet(self):
        if (self._toan <= 2 or self._ly <= 2 or self._hoa <= 2):
            return True


class SinhVienB(Student):
    def __init__(self, cccd, sbd, ho_ten, dia_chi, toan, sinh, hoa):
        super().__init__(cccd, sbd, ho_ten, dia_chi)
        self._toan = self._check_toan(toan)
        self._sinh = self._check_sinh(sinh)
        self._hoa = self._check_hoa(hoa)

    # get
    def get_toan(self):
        return self._toan

    def get_sinh(self):
        return self._sinh

    def get_hoa(self):
        return self._hoa

    # set
    def set_toan(self, toan):
        self._toan = self._check_toan(toan)

    def set_sinh(self, sinh):
        self._sinh = self._check_sinh(sinh)

    def set_hoa(self, hoa):
        self._hoa = self._check_hoa(hoa)

    # check điểm toán
    def _check_toan(self, toan):
        try:
            toan = float(toan)
            if toan < 0 or toan > 10:
                raise ValueError("Điểm toán không hợp lệ")
            return toan
        except ValueError:
            raise ValueError("Điểm toán phải là số thực")

    # check điểm lý
    def _check_sinh(self, sinh):
        try:
            sinh = float(sinh)
            if sinh < 0 or sinh > 10:
                raise ValueError("Điểm sinh không hợp lệ")
            return sinh
        except ValueError:
            raise ValueError("Điểm sinh phải là số thực")

    # check điểm hóa
    def _check_hoa(self, hoa):
        try:
            hoa = float(hoa)
            if hoa < 0 or hoa > 10:
                raise ValueError("Điểm hóa không hợp lệ")
            return hoa
        except ValueError:
            raise ValueError("Điểm hóa phải là số thực")

    # get điểm trung bình
    def get_diem_tb(self):
        return ((self._toan + self._sinh)+self._hoa) / 3

    # get thông tin
    def get_info(self):
        print(
            f"CCCD: {self._cccd}, SBD: {self._sbd}, Họ tên: {self._ho_ten}, Địa chỉ: {self._dia_chi}, Điểm toán: {self._toan}, Điểm sinh: {self._sinh}, Điểm hóa: {self._hoa}")

    # get điểm:
    def get_tong_diem(self):
        return self._toan + self._sinh + self._hoa * 1.5

    # check liệt: môn nào điểm dưới 2 thì học sinh đó liệt
    def check_liet(self):
        if (self._toan <= 2 or self._sinh <= 2 or self._hoa <= 2):
            return True

class ManageStudent:
    def __init__(self):
        self._list_sinhvienA = []
        self._list_sinhvienB = []
        #gộp 2 list sinh viên A và sinh viên B thành 1 list sinh viên
        self._list_sinhvien = self._list_sinhvienA + self._list_sinhvienB

    # thêm sinh viên
    def add_student(self, student):
        if isinstance(student, SinhVienA):
            for i in self._list_sinhvienA:
                if i.get_sbd() == student.get_sbd():
                    raise ValueError("Số báo danh đã tồn tại")
                if i.get_cccd() == student.get_cccd():
                    raise ValueError("Căn cước công dân đã tồn tại")
            self._list_sinhvienA.append(student)
            self._list_sinhvien.append(student)
        elif isinstance(student, SinhVienB):
            for i in self._list_sinhvienB:
                if i.get_sbd() == student.get_sbd() or i.get_cccd() == student.get_cccd():
                    raise ValueError("Số báo danh đã tồn tại")
                if i.get_cccd() == student.get_cccd():
                    raise ValueError("Căn cước công dân đã tồn tại")
            self._list_sinhvienB.append(student)
            self._list_sinhvien.append(student)
        else:
            raise ValueError("Không phải là sinh viên")
    # cập nhật thông tin sinh viên
    def update_student_info(self, sbd):
        for student in self._list_sinhvien:
            if student.get_sbd() == sbd:
                print(f"Chọn thông tin cần sửa cho thí sinh có số báo danh {sbd}:")
                print("1. Căn cước công dân")
                print("2. Họ tên")
                print("3. Địa chỉ")

                if isinstance(student, SinhVienA):
                    print("4. Điểm toán")
                    print("5. Điểm lý")
                    print("6. Điểm hóa")

                elif isinstance(student, SinhVienB):
                    print("4. Điểm toán")
                    print("5. Điểm sinh")
                    print("6. Điểm hóa")

                choice = input("Chọn thông tin cần sửa (1-6): ")

                if choice == '1':
                    new_cccd = input("Nhập mới Căn cước công dân: ")
                    student.set_cccd(new_cccd)

                elif choice == '2':
                    new_ho_ten = input("Nhập mới Họ tên: ")
                    student.set_ho_ten(new_ho_ten)

                elif choice == '3':
                    new_dia_chi = input("Nhập mới Địa chỉ: ")
                    student.set_dia_chi(new_dia_chi)

                elif choice in ('4', '5', '6') and isinstance(student, (SinhVienA, SinhVienB)):
                    new_diem = float(input("Nhập mới điểm: "))
                    if choice == '4':
                        student.set_toan(new_diem)
                    elif choice == '5':
                        if isinstance(student, SinhVienA):
                            student.set_ly(new_diem)
                        elif isinstance(student, SinhVienB):
                            student.set_sinh(new_diem)
                    elif choice == '6':
                        student.set_hoa(new_diem)

                else:
                    print("Lựa chọn không hợp lệ.")

                print("Cập nhật thông tin thành công!")
                return

        print(f"Không tìm thấy thí sinh có số báo danh {sbd}.")
    # xóa sinh viên theo số báo danh
    def remove_student(self, sbd):
        for i in self._list_sinhvien:
            if i.get_sbd() == sbd:
                self._list_sinhvien.remove(i)
                if isinstance(i, SinhVienA):
                    self._list_sinhvienA.remove(i)
                else:
                    self._list_sinhvienB.remove(i)
                return True
        return False

    # tìm kiếm sinh viên theo số báo danh hoặc căn cước công dân và trả về thông tin sinh viên
    def find_student_by_sbd(self, sbd):
        for i in self._list_sinhvien:
            if i.get_sbd() == sbd:
                i.get_info()

    def find_student_by_cccd(self, cccd):
        for i in self._list_sinhvien:
            if i.get_cccd() == cccd:
                i.get_info()

    # sort danh sách sinh viên A theo tổng điểm tăng dần hoặc giảm dần
    def sort_SinhVienA_by_tong_diem_tang(self):
        self._list_sinhvienA.sort(key=lambda x: x.get_tong_diem(), reverse=False)
        print("Danh sách sinh viên khối A theo thứ tự tăng dần theo tổng điểm:")
        for i in self._list_sinhvienA:
            i.get_info()

    def sort_SinhVienA_by_tong_diem_giam(self):
        self._list_sinhvienA.sort(key=lambda x: x.get_tong_diem(), reverse=True)
        print("Danh sách sinh viên khối A theo thứ tự giảm dần theo tổng điểm:")
        for i in self._list_sinhvienA:
            i.get_info()

    #sort danh sách sinh viên B theo tổng điểm tăng dần hoặc giảm dần
    def sort_SinhVienB_by_tong_diem_tang(self):
        self._list_sinhvienB.sort(key=lambda x: x.get_tong_diem(), reverse=False)
        print("Danh sách sinh viên khối B theo thứ tự tăng dần theo tổng điểm:")
        for i in self._list_sinhvienB:
            i.get_info()

    def sort_SinhVienB_by_tong_diem_giam(self):
        self._list_sinhvienB.sort(key=lambda x: x.get_tong_diem(), reverse=True)
        print("Danh sách sinh viên khối B theo thứ tự giảm dần theo tổng điểm:")
        for i in self._list_sinhvienB:
            i.get_info()

    #danh sách sinh viên không liệt
    def list_sinh_vien_khong_liet(self):
        print("Danh sách sinh viên không liệt môn nào:")
        for i in self._list_sinhvien:
            if i.check_liet() != True:
                i.get_info()

    # thống kê danh sách thí sinh đạt học bống theo từng loại sinhvienA hoặc sinh viên B, điều kiện là tổng điểm > 32
    def thong_ke_sinh_vien_dat_hoc_bong(self):
        list_sinh_vien_dat_hoc_bong_A = []
        list_sinh_vien_dat_hoc_bong_B = []
        for i in self._list_sinhvienA:
            if i.get_tong_diem() > 32:
                list_sinh_vien_dat_hoc_bong_A.append(i)
        for i in self._list_sinhvienB:
            if i.get_tong_diem() > 32:
                list_sinh_vien_dat_hoc_bong_B.append(i)

        print("Danh sách sinh viên đạt học bổng loại A top 5:")
        # kiểm tra xem có sinh viên đạt học bổng loại A không
        if len(list_sinh_vien_dat_hoc_bong_A) == 0:
            print("Không có sinh viên đạt học bổng loại A")
        else:
            # sắp xếp danh sách sinh viên A đạt học bổng theo thứ tự giảm dần
            list_sinh_vien_dat_hoc_bong_A.sort(key=lambda x: x.get_tong_diem(), reverse=True)
            #danh sách
            for i in list_sinh_vien_dat_hoc_bong_A[0:5]:
                i.get_info()

        print("Danh sách sinh viên đạt học bổng loại B:")
        # kiểm tra xem có sinh viên đạt học bổng loại B không
        if len(list_sinh_vien_dat_hoc_bong_B) == 0:
            print("Không có sinh viên đạt học bổng loại B")
        else:
            # sắp xếp danh sách sinh viên B đạt học bổng theo thứ tự giảm dần
            list_sinh_vien_dat_hoc_bong_B.sort(key=lambda x: x.get_tong_diem(), reverse=True)
            #danh sách
            for i in list_sinh_vien_dat_hoc_bong_B[0:5]:
                i.get_info()

    def get_danh_sach_sinh_vien_A(self):
        print("Danh sách sinh viên khối A:")
        for i in self._list_sinhvienA:
            i.get_info()

    def get_danh_sach_sinh_vien_B(self):
        print("Danh sách sinh viên khối B:")
        for i in self._list_sinhvienB:
            i.get_info()

def main():
    # Tạo đối tượng quản lý sinh viên
    manager = ManageStudent()

    while True:
        print("\n------ MENU ------")
        print("1. Thêm mới thí sinh.")
        print("2. Tìm kiếm thí sinh.")
        print("3. Sửa thông tin thí sinh.")
        print("4. Xoá thí sinh.")
        print("5. Hiển thị danh sách thí sinh có tổng điểm 3 môn theo thứ tự tăng dần hoặc giảm dần.")
        print("6. Hiển thị danh sách thí sinh đạt học bổng.")
        print("7. Hiển thị danh sách thí sinh không liệt môn nào.")
        print("8. Hiển thị danh sách thí sinh theo từng khối")
        print("9. Thoát chương trình.")

        choice = input("Chọn chức năng (1-8): ")

        if choice == '1':
            try:
                # Thêm mới thí sinh
                student_type = input("Chọn loại sinh viên (A/B): ")
                if student_type.upper() == 'A':
                    student = SinhVienA(input("CCCD: "), input("SBD: "), input("Họ tên: "), input("Địa chỉ: "),
                                        float(input("Điểm lý: ")), float(input("Điểm lý: ")), float(input("Điểm hóa: ")))
                elif student_type.upper() == 'B':
                    student = SinhVienB(input("CCCD: "), input("SBD: "), input("Họ tên: "), input("Địa chỉ: "),
                                        float(input("Điểm toán: ")), float(input("Điểm toán: ")), float(input("Điểm hóa: ")))
                else:
                    print("Loại sinh viên không hợp lệ.")
                    continue

                manager.add_student(student)
                print("Thêm thành công!")

            except ValueError as e:
                print(f"Lỗi: {e}")

        elif choice == '2':
            sbd_or_cccd = input("Nhập số báo danh hoặc căn cước công dân: ")
            manager.find_student_by_sbd(sbd_or_cccd)
            manager.find_student_by_cccd(sbd_or_cccd)

        elif choice == '3':
            sbd_to_update = input("Nhập số báo danh của thí sinh cần cập nhật thông tin: ")
            manager.update_student_info(sbd_to_update)

        elif choice == '4':
            sbd_to_remove = input("Nhập số báo danh của thí sinh cần xoá: ")
            if manager.remove_student(sbd_to_remove):
                print("Xoá thành công!")
            else:
                print("Không tìm thấy thí sinh có số báo danh cần xoá.")

        elif choice == '5':
            sort_order = input("Chọn thứ tự sắp xếp (tang/giam): ")
            if sort_order.lower() == 'tang':
                manager.sort_SinhVienA_by_tong_diem_tang()
                manager.sort_SinhVienB_by_tong_diem_tang()
            elif sort_order.lower() == 'giam':
                manager.sort_SinhVienA_by_tong_diem_giam()
                manager.sort_SinhVienB_by_tong_diem_giam()
            else:
                print("Thứ tự sắp xếp không hợp lệ.")

        elif choice == '6':
            manager.thong_ke_sinh_vien_dat_hoc_bong()

        elif choice == '7':
            manager.list_sinh_vien_khong_liet()

        elif choice == '8':
            manager.get_danh_sach_sinh_vien_A()
            manager.get_danh_sach_sinh_vien_B()

        elif choice == '9':
            print("Chương trình kết thúc.")
            break

        else:
            print("Chức năng không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()

