# 7:49

# Câu 1:
# s = input().upper()
# a = {}
# for i in s:
#     if i.isalpha():
#         if i not in a:
#             a[i] = 1
#         else:
#             a[i] += 1
# for i in a:
#     print(i+':'+str(a[i]))
# dem = 0
# for i in s:
#     if i!=' ':
#         dem += 1
# print(dem)

# Câu 2:
# def check(s):
#     dem = 0
#     for i in s:
#         if i=='0' or i=='1': dem += 0
#         else: dem += 1
#     if dem==0: return 1
#     else: return 0
# s = input()
# if check(s)==1:
#     x = int(s)
#     sum = i = 0
#     while(x!=0):
#         sum += (x%10) * 2**i
#         x //= 10
#         i += 1
# print(sum)

# Câu 3:
# n,m = map(int,input().split())
# a = []
# for i in range(n):
#     x = list(map(int,input().split()))
#     a.append(x)
# for i in range(m):
#     for j in range(n):
#         print(a[j][i],end=' ')
#     print()

# Câu 4:
class Khachang:
    def __init__(self):
        self.mkh = ''
        self.ht = ''
        self.dc = ''
        self.csc = 0
        self.csm = 0
    def nhap(self):
        self.mkh = input('\nNhap ma khach hang: ')
        self.ht = input('Nhap ho ten: ')
        self.dc = input('Nhap dia chi: ')
        self.csc = int(input('Nhap chi so cu: '))
        self.csm = int(input('Nhap chi so moi: '))
    def xuat(self):
        print('-------------------------')
        print('Ma khach hang:',self.mkh)
        print('Ho ten:',self.ht)
        print('Dia chi:',self.dc)
        print('SLDSD:',self.csm - self.csc)
        print('-------------------------')
class Quanly:
    def __init__(self):
        self.td = {}
        self.a = []
        self.n = 0
    def nhapds(self):
        self.n = int(input('Nhap so luong khach hang: '))
        for i in range(self.n):
            x = Khachang()
            while 1:
                x.nhap()
                if x.mkh not in self.td:
                    self.td[x.mkh] = 1
                    self.a.append(x)
                    break
                elif x.mkh in self.td:
                    print('\nNhap lai vi trung ma khach hang !!!')
    def tk(self):
        dem = 0
        for i in self.a:
            if 'kh102' in i.mkh.lower(): dem += i.csm - i.csc
        print("\nSố lượng điện người sủ dụng có chứa mã \"KH102\":", dem)
    def xuatds(self):
        max = 0
        for i in self.a:
            if max < i.csm - i.csc:
                max = i.csm - i.csc
        print("\nNhững người có lượng điện lớn nhất: ")
        for i in self.a:
            if max == i.csm - i.csc:
                i.xuat()
x = Quanly()
x.nhapds()
x.tk()
x.xuatds()



# class HoaDon:
#     def __init__(self):
#         self.mkh = ""
#         self.diachi = ""
#         self.hoten = ""
#         self.csc = 0
#         self.csm = 0
#     def tinhtiendien(self):
#         return self.csm - self.csc
#     def nhap(self):
#         self.mkh = input("Nhập mã khách hàng: ")
#         self.hoten = input("Nhập tên khách hàng: ")
#         self.diachi = input("Nhập địa chỉ: ")
#         self.csc = int(input("Nhập chỉ số cũ: "))
#         self.csm = int(input("Nhập chỉ số mới: "))
#     def xuat(self):
#         print("Mã Khách hàng la:", self.mkh)
#         print("Tên Khách hàng là:",self.hoten)
#         print("Địa chỉ là:",self.diachi)
#         print("Chỉ số cũ là:",self.csc)
#         print("Chỉ số mới là:",self.csm)
# class QuanLy:
#     def __init__(self):
#         self.mp = {}
#         self.A = []
#         self.n = 0
#     def nhap(self):
#         self.n = int(input("Nhập số lượng khách hàng: "))
#         for i in range(self.n):
#             x = HoaDon()
#             while (1):
#                 x.nhap()
#                 if (x.mkh not in self.mp):
#                     self.mp[x.mkh] = True
#                     self.A.append(x)
#                     break
#                 print("Nhap lai thông tin (Trùng mã): ")
#     def thongke(self):
#         sl = 0
#         for i in self.A:
#             if ("KH102" in i.mkh.upper()): sl += i.tinhtiendien()
#         print("Số lượng điện người sủ dụng có chứa mã \"KH102\":", sl)
#     def innguoidungnhieu(self):
#         mx = 0
#         print("Những người có lượng điện lớn nhất: ")
#         for i in self.A:
#             mx = max(mx, i.tinhtiendien())
#         for i in self.A:
#             if (mx == i.tinhtiendien()):
#                 i.xuat()
# x = QuanLy()
# x.nhap()
# x.thongke()
# x.innguoidungnhieu()

