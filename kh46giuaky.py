# def check(s):
#     a = {}
#     for i in s.split():
#         if i not in a:
#             a[i] = 0
#     return len(a)
# s = input()
# print(check(s))

# n,m = map(int,input().split())
# a = []
# for i in range(n):
#     x = list(map(int,input().split()))
#     a.append(x) 
# for i in range(n):
#     for j in range(m):
#         print(a[i][j],end=" ")
#     print()
    

# n = int(input())
# a = []
# for i in range(n):
#     x = list(map(int,input().split()))
#     a.append(x)
# m = int(input())
# for i in range(n):
#     if a[m][i] == 1:
#         print(i,end=' ')

class Khachhang:
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
        print('------------------------')
        print('Ma khach hang:',self.mkh)
        print('Ho va ten:',self.ht)
        print('Dia chi:',self.dc)
        print('------------------------')
    
    
a = []
n = int(input('Nhap so khach hang: '))
for i in range(n):
    x = Khachhang()
    x.nhap()
    a.append(x)
dem = 0
for i in a:
    if 'kh102' in i.mkh.lower():
        dem += 1
print('\nKhach hang co ma (KH102): ',end='') 
print(dem)
max = 0
for i in a:
    if (i.csm - i.csc) > max:
        max = i.csm - i.csc
print('\nDanh sach khach hang su dung dien lon nhat !!!')
for i in a:
    if max == (i.csm - i.csc):
        i.xuat()


