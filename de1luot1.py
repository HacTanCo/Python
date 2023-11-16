# Câu 1:
# def check(s):
#     return s.split()[-1]

# dem = 0
# oke = True
# while oke:
#     s = input('Nhập tên: ')
#     if s=='':
#         break
#     if check(s).lower() == 'anh':
#         dem += 1
# print('Số lượng sinh viên tên Anh: ',dem)

# Câu 2:
# n = int(input('Nhap danh sach hoc phan n < 10: '))
# while n>=10:
#     n = int(input('Nhap lai n < 10: '))
    
# a = []
# for i in range(n):
#     mhp = input('\nNhap ma hoc phan: ')
#     thp = input('Nhap ten hoc phan: ')
#     stc =int(input('Nhap so tin chi: '))
#     a.append({'mahp':mhp, 'tenhp':thp, 'sotc':stc})

# print('\nDanh sach ma hoc phan co 3 ky tu dau la TIN !!!')
# for i in a:
#     if i['mahp'][0:3].upper() == 'TIN':
#         print(i) 

# s = input('\nNhap chuoi: ')
# print('\nDanh sach hoc phan co chua chuoi s: ',end='')
# for i in a:
#     if s.upper() in i['tenhp'].upper():
#             print(i['tenhp'],end=',')

# Câu 3 and 4:
# class hoadon:
#     def __init__(self):
#         self.mkh = ''
#         self.ht = ''
#         self.dc = ''
#         self.csc = 0
#         self.csm = 0
#     def get_mkh(self):
#         return self.mkh
#     def get_ldtt(self):
#         return self.csm - self.csc
#     def fill(self):
#         self.mkh = input('\nNhap ma khach hang: ')
#         self.ht = input('Nhap ho ten: ')
#         self.dc = input('Nhap dia chi: ')
#         self.csc = int(input('Nhap chi so cu: '))
#         self.csm = int(input('Nhap chi so moi: '))
#     def show(self):
#         print('------------------------------------')
#         print('Ma khach hang:',self.mkh)
#         print('Ho ten:',self.ht)
#         print('Dia chi:',self.dc)
#         print('Luong dien tieu thu:',self.get_ldtt())
#         print('------------------------------------')
#     def __gt__(self , other):
#         return self.get_ldtt() > other.get_ldtt()

# class quanly:
#     def __init__(self):
#         self.n = 0
#         self.arr = []
#         self.td = {}
#     def fillds(self):
#         self.n = int(input('Nhap so luong hoa don (n <= 50): '))
#         while self.n > 50:
#             self.n = int(input('Nhap lai: '))
#         for i in range(self.n):
#             x = hoadon()
#             while 1:
#                 x.fill()
#                 if x.mkh not in self.td:
#                     self.td[x.mkh] = 1
#                     self.arr.append(x)
#                     break
#                 elif x.mkh in self.td:
#                     print('\nNhap lai vi trung ma khach hang: ')
#     def sort(self):
#         for i in range(0, self.n-1):
#             for j in range(i+1, self.n):
#                 if self.arr[i] > self.arr[j]:
#                     x = hoadon()
#                     x = self.arr[i]
#                     self.arr[i] = self.arr[j]
#                     self.arr[j] = x
#         print('\nDanh sach tang dan theo luong dien tieu thu !!!')
#         for i in self.arr:
#             i.show()
                
#     def ma(self):
#         dem = 0
#         print('\nDanh sach ma khach hang co ma bang ma !!!')
#         for i in self.arr:
#             if 'ma' in i.mkh.lower():
#                 dem += 1
#                 i.show()
#         if dem == 0:
#             print('Khong ton tai khach hang nay !!!')
#     def luufile(self):
#         with open('C:/Users/Administrator/Desktop/HTC/Python/KhachHang.txt','w') as file:
#             for i in self.arr:
#                 if i.get_ldtt() > 100:
#                     mkh1 = i.mkh
#                     ht1 = i.ht
#                     dc1 = i.dc
#                     file.write(mkh1 + ';' + ht1 + ';' + dc1 + '\n')
#             file.close()


# x = quanly()
# x.fillds()
# x.sort()
# x.ma()
# x.luufile()



class hoadon:
    def __init__(a):
        a.mkh = ''
        a.ht = ''
        a.dc = ''
        a.csc = 0
        a.csm = 0
    def get_mkh(a):
        return a.mkh
    def get_luongdien(a):
        return a.csm - a.csc
    def fillhd(a):
        a.mkh = input('\nNhập mã khách hàng: ')
        a.ht = input('Nhập họ tên: ')
        a.dc = input('Nhập địa chỉ: ')
        a.csc = int(input('Nhập chỉ số cũ: '))
        a.csm = int(input('Nhập chỉ số mới: '))
    def showhd(a):
        print('------------------------------')
        print('Mã khách hàng:',a.mkh)
        print('Họ tên:',a.ht)
        print('Địa chỉ:',a.dc)
        print('Lượng điện tiêu thụ:',a.get_luongdien())
        print('------------------------------')
    def __gt__(a,b):
        return a.get_luongdien() > b.get_luongdien()
    
class quanly:
    def __init__(a):
        a.n = 0
        a.arr = []
        a.td = {}
    def fillql(a):
        a.n = int(input('Nhập số lượng hóa đơn: '))
        while a.n <= 0 or a.n >50:
            a.n = int(input('Nhập lại: '))
        
        for i in range(a.n):
            x = hoadon()
            while True:
                x.fillhd()
                if x.mkh not in a.td:
                    a.td[x.mkh] = 1
                    a.arr.append(x)
                    break
                print('\nNhap lai vi trung ma khach hang: ')
    def sort(a):
        for i in range(0,a.n-1):
            for j in range(i+1,a.n):
                if a.arr[i] > a.arr[j]:
                    x = hoadon()
                    x = a.arr[i]
                    a.arr[i] = a.arr[j]
                    a.arr[j] = x
        
        print('\nDanh sách tăng dần theo lượng điện tiêu thụ !!!')
        for i in a.arr:
            i.showhd()
    def ma(a):
        s = input('\nNhập chuỗi: ')
        dem = 0
        print('\nDanh sách khách hàng có mã bằng ma !!!')
        for i in a.arr:
            if s.lower() == i.mkh.lower():
                i.showhd()
                dem += 1
        if dem==0:
            print('\nKhông tồn tại mã khách hàng này')
    def luufile(a):
        with open('C:/Users/Administrator/Desktop/HTC/Python/KhachHang.txt','w') as file:
            for i in a.arr:
                if i.get_luongdien() > 100:
                    mkh1 = i.mkh
                    ht1 = i.ht
                    dc1 = i.dc
                    file.write(mkh1 + ';' + ht1 + ';' + dc1 + '\n')
            file.close()


x = quanly()
x.fillql()
x.sort()
x.ma()
x.luufile()