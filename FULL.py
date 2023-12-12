from datetime import datetime
class Vehicle:
    def __init__(self,mpt='',tpt='',nsx=0,gb=0,nbdsd=0):
        self.mpt = mpt
        self.tpt = tpt
        self.nsx = nsx
        self.gb = gb
        self.nbdsd = nbdsd

    def set_mpt(self,mpt):
        self.mpt = mpt
    def get_mpt(self):
        return self.mpt
    
    def set_tpt(self,tpt):
        self.tpt = tpt
    def get_tpt(self):
        return self.tpt
    
    def set_nsx(self,nsx):
        self.nsx = nsx
    def get_nsx(self):
        return self.nsx
    
    def set_gb(self,gb):
        self.gb = gb
    def get_gb(self):
        return self.gb
    
    def set_nbdsd(self,nbdsd):
        self.nbdsd = nbdsd
    def get_nbdsd(self):
        return self.nbdsd
    
    def fill(self):
        self.mpt = input('Nhập mã phương tiện: ')
        self.tpt = input('Nhập tên phương tiện: ')
        self.nsx = int(input('Nhập năm sản xuất: '))
        self.gb = int(input('Nhập giá bán: '))
        self.nbdsd = int(input('Nhập năm bắt đầu sử dụng: '))
    def show(self):
        print('-----------------------------')
        print('Mã phương tiện:',self.mpt)
        print('Tên phương tiện:',self.tpt)
        print('Năm sản xuất:',self.nsx)
        print('Giá bán:',self.gb)
        print('Nắm bắt đầu sử dụng:',self.nbdsd)
        print('-----------------------------')
    def __gt__(self,other):
        return self.get_gb() > other.get_gb()

class Car(Vehicle):
    def __init__(self, mpt='', tpt='', nsx=0, gb=0, nbdsd=0,scn=0,dtdc=0,lnl=''):
        super().__init__(mpt, tpt, nsx, gb, nbdsd)
        self.scn = scn
        self.dtdc = dtdc
        self.lnl = lnl
    def set_scn(self,scn):
        self.scn = scn
    def get_scn(self):
        return self.scn
    
    def set_dtdc(self,dtdc):
        self.dtdc = dtdc
    def get_dtdc(self):
        return self.dtdc
    
    def set_lnl(self,lnl):
        self.lnl = lnl
    def get_lnl(self):
        return self.lnl
    
    def fillcar(self):
        super().fill()
        self.scn = int(input('Nhập số chỗ ngồi: '))
        self.dtdc = int(input('Nhập dung tích động cơ: '))
        while 1:
            self.lnl = input('Nhập loại nhiên liệu: ')
            if self.lnl.lower()=='xăng' or self.lnl.lower()=='dầu diesel':
                break
            else:
                print('Nhập lại!!!')
    def tgsdcar(self):
        return datetime.now().year - self.nsx
    def giatrisudungcar(self):
        if self.tgsdcar()<3:
            return 0.85 * self.get_gb()
        elif 3<= self.tgsdcar() <=6:
            return 0.75 * self.get_gb()
        elif 6<= self.tgsdcar() <=10:
            return 0.6 * self.get_gb()
        else:
            return 0.3 * self.get_gb()
class Motobike(Vehicle):
    def __init__(self, mpt='', tpt='', nsx=0, gb=0, nbdsd=0,pk=0):
        Vehicle.__init__(self,mpt,tpt,nsx,gb,nbdsd)
        self.pk = pk
    def set_pk(self,pk):
        self.pk = pk
    def get_pk(self):
        return self.pk
    
    def fillMoto(self):
        super().fill()
        self.pk = int(input('Nhập phân khối: '))
    def tgsdmoto(self):
        return datetime.now().year - self.nsx
    def giatrisudungmoto(self):
        if self.tgsdmoto()<5:
            return 0.8 * self.get_gb()
        elif 5<= self.tgsdmoto()<=10:
            return 0.5 * self.get_gb()
        else:
            return 0.3 * self.get_gb()

class Quanly:
    def __init__(self):
        self.n = 0
        self.arr = []
        self.arrc = []
        self.arrm = []
        self.tdc = {}
        self.tdm = {}
    def fillql(self):
        self.n = int(input('Nhập số lượng xe oto và xe máy: '))
        while self.n<=0 or self.n>50:
            self.n = int(input('Nhập lại: '))  
        lx = 0
        for i in range(self.n):
            while 1:
                lx = int(input('\nNhập 1-Car, 2-Motobike: '))
                if lx==1 or lx==2:break
                print('Nhap lai !!!')
            if lx==1:
                x = Car()
                while 1:
                    x.fillcar()
                    if x.mpt not in self.tdc:
                        self.tdc[x.mpt] = 1
                        self.arrc.append(x)
                        break
                    print('Nhap lai trung ma !!!')
            elif lx==2:
                x = Motobike()
                while 1:
                    x.fillMoto()
                    if x.mpt not in self.tdm:
                        self.tdm[x.mpt] = 1
                        self.arrm.append(x)
                        break
                    print('Nhap lai trung ma !!!')
    def showql(self):
        mincar = self.arrc[0].giatrisudungcar()
        for i in self.arrc:
            if i.giatrisudungcar() > mincar: mincar = i.giatrisudungcar()  
        print('\nDanh sach Car có giá trị sử dụng thấp nhất !!!')
        for i in self.arrc:
            if i.giatrisudungcar()==mincar: i.show()  

        minmoto = self.arrm[0].giatrisudungmoto()
        for i in self.arrm:
            if i.giatrisudungmoto() > minmoto: minmoto = i.giatrisudungmoto()   
        print('\nDanh sach Moto có giá trị sử dụng thấp nhất !!!')
        for i in self.arrm:
            if i.giatrisudungmoto()==minmoto: i.show()  
        
x = Quanly()
x.fillql()
x.showql()

# from datetime import datetime

# class Vehicle:
#     def __init__(self):
#         self.ma_phuong_tien = None
#         self.ten_phuong_tien = None
#         self.nam_san_xuat = None
#         self.gia_ban = None

#     def nhap_du_lieu(self):
#         self.ma_phuong_tien = input("Nhập mã phương tiện: ")
#         self.ten_phuong_tien = input("Nhập tên phương tiện: ")
#         self.nam_san_xuat = int(input("Nhập năm sản xuất: "))
#         self.gia_ban = float(input("Nhập giá bán: "))

#     def hien_thi_thong_tin(self):
#         print(f"Mã phương tiện: {self.ma_phuong_tien}")
#         print(f"Tên phương tiện: {self.ten_phuong_tien}")
#         print(f"Năm sản xuất: {self.nam_san_xuat}")
#         print(f"Giá bán: {self.gia_ban}")

#     def __gt__(self, other):
#         return self.gia_ban > other.gia_ban

# class Car(Vehicle):
#     def __init__(self):
#         super().__init__()
#         self.so_cho_ngoi = None
#         self.dung_tich_dong_co = None
#         self.loai_nhien_lieu = None

#     def nhap_du_lieu(self):
#         super().nhap_du_lieu()
#         self.so_cho_ngoi = int(input("Nhập số chỗ ngồi: "))
#         self.dung_tich_dong_co = int(input("Nhập dung tích động cơ (cm^3): "))
#         self.loai_nhien_lieu = input("Nhập loại nhiên liệu (xăng/dầu diesel): ")

#     def hien_thi_thong_tin(self):
#         super().hien_thi_thong_tin()
#         print(f"Số chỗ ngồi: {self.so_cho_ngoi}")
#         print(f"Dung tích động cơ: {self.dung_tich_dong_co} cm^3")
#         print(f"Loại nhiên liệu: {self.loai_nhien_lieu}")

#     def thoi_gian_su_dung(self):
#         return datetime.now().year - self.nam_san_xuat

#     def gia_tri_su_dung(self):
#         thoi_gian_su_dung = self.thoi_gian_su_dung()
#         if thoi_gian_su_dung < 5:
#             return self.gia_ban * 0.8
#         elif thoi_gian_su_dung < 10:
#             return self.gia_ban * 0.5
#         else:
#             return self.gia_ban * 0.3

# class Motobike(Vehicle):
#     def __init__(self):
#         super().__init__()
#         self.phan_khoi = None

#     def nhap_du_lieu(self):
#         super().nhap_du_lieu()
#         self.phan_khoi = int(input("Nhập phân khối (cm^3): "))

#     def hien_thi_thong_tin(self):
#         super().hien_thi_thong_tin()
#         print(f"Phân khối: {self.phan_khoi} cm^3")

#     def thoi_gian_su_dung(self):
#         return datetime.now().year - self.nam_san_xuat

#     def gia_tri_su_dung(self):
#         thoi_gian_su_dung = self.thoi_gian_su_dung()
#         if thoi_gian_su_dung < 3:
#             return self.gia_ban * 0.85
#         elif thoi_gian_su_dung < 6:
#             return self.gia_ban * 0.75
#         elif thoi_gian_su_dung < 10:
#             return self.gia_ban * 0.6
#         else:
#             return self.gia_ban * 0.4

# danh_sach_xe = []
# n = int(input("Nhập số lượng xe (n <= 50): "))

# for i in range(n):
#     loai_xe = input("Nhập loại xe (ô tô/xe máy): ")
    
#     if loai_xe.lower() == "ô tô":
#         xe = Car()
#     elif loai_xe.lower() == "xe máy":
#         xe = Motobike()
#     else:
#         print("Loại xe không hợp lệ. Vui lòng nhập lại.")
#         continue

#     xe.nhap_du_lieu()
    
#     if any(x.ma_phuong_tien == xe.ma_phuong_tien for x in danh_sach_xe):
#         print("Mã xe đã tồn tại. Vui lòng nhập lại.")
#     else:
#         danh_sach_xe.append(xe)

# xe_may = [xe for xe in danh_sach_xe if isinstance(xe, Motobike)]
# if xe_may:
#     gia_tri_con_lai_thap_nhat = min(xe.gia_tri_su_dung() for xe in xe_may)
#     xe_may_gia_tri_con_lai_thap_nhat = [xe for xe in xe_may if xe.gia_tri_su_dung() == gia_tri_con_lai_thap_nhat]
    
#     print("Xe máy có giá trị còn lại thấp nhất:")
#     for xe in xe_may_gia_tri_con_lai_thap_nhat:
#         xe.hien_thi_thong_tin()
# else:
#     print("Không có xe máy nào trong danh sách.")