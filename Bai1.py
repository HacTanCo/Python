from math import *
class phanso:
    def __init__(self):
        self.t = 0
        self.m = 1

    def nhap(self):
        self.t = int(input('Nhap tu: '))
        self.m = int(input('Nhap mau: '))
        while self.m == 0:
           self.m = int(input('Nhap lai (mau != 0): ')) 

    def tg(self):
        x = gcd(self.t,self.m)
        self.t //= x
        self.m //= x

    def xuat(self):
        print(self.t,'/',self.m)

    def __add__(self,other):
        p = phanso()
        p.t = self.t * other.m + other.t * self.m
        p.m = self.m * other.m
        p.tg()
        return p
    
    def __sub__(self,other):
        p = phanso()
        p.t = self.t * other.m - other.t * self.m
        p.m = self.m * other.m
        p.tg()
        return p
    
    def __mul__(self,other):
        p = phanso()
        p.t = self.t * other.t
        p.m = self.m * other.m
        p.tg()
        return p
    
    def __truediv__(self,other):
        p = phanso()
        p.t = self.t * other.m
        p.m = self.m * other.t
        p.tg()
        return p
    
    def __lt__(self,other):
        return self.t * other.m < other.t * self.m
    
    def __iadd__(self,other):
        self.t = self.t * other.m + other.t * self.m
        self.m = self.m * other.m
        self.tg()
        return self
    
class quanly:
    def __init__(self):
        self.n = 0
        self.a = []

    def nhapds(self):
        self.n = int(input('So luong phan so: '))
        while self.n <= 0:
            self.n = int(input('Nhap lai ( danh sach > 0): '))
        for i in range(self.n):
            x = phanso()
            x.nhap()
            self.a.append(x)

    def bot1(self):
        mn = min(self.a)
        print('Phan so nho nhat: ',end='')
        mn.xuat()

    def sumall(self):
        sum = phanso()
        for i in self.a:   
            sum += i
        print('Tong cac phan so trong danh sach: ',end='')
        sum.xuat()



x = quanly()
x.nhapds()
x.bot1()
x.sumall()