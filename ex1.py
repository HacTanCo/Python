# class ac:
#     def __init__(a,ht='',sd=0):
#         a.ht = ht
#         a.sd = sd
#     def fill(a):
#         a.ht = input()
#         a.sd = int(input())
#     def show(a):
#         print(a.ht+',',end='')
#         print(a.sd)
#     def nap(a,x):
#         if x>=5000:
#             a.sd += x
#         elif x<5000:
#             print('No recharge')
#     def rut(a,x):
#         if 2000<=x<=a.sd:
#             a.sd -= x
#         else:
#             print('No withdraw')
# n1 = input()
# t1 = int(input())
# x = ac(n1)
# x.nap(t1)
# x.show()
# n2 = input()
# t2 = int(input())
# y = ac(n2,t2)
# y.show()
# t3 = int(input())
# y.rut(t3)
# y.show()

class MaTran:
    def __init__(self,n = 0,m = 0):
        self.n = n
        self.m = m
        self.A = []
    def nhap(self):
        self.n , self.m = map(int, input().split())
        for i in range(0, self.n):
            while (1):
                x = list(map(int, input().split()))
                if (len(x) == self.m): break
                print("Nhập lại")
            self.A.append(x)
    def xuat(self):
        for i in range(self.n):
            for j in range(self.m):
                print(self.A[i][j], end= ' ')
            print()
    def nhanduoc(self,other):
        return self.m == other.n
    def congduoc(self,other):
        return (self.n == other.n and self.m == other.m)
    def __add__(self, other):
        C = MaTran(self.n,self.m)
        for i in range(self.n):
            Hang = []
            for j in range(self.m):
                Hang.append(self.A[i][j] + other.A[i][j])
            C.A.append(Hang)
        return C
    def __mul__(self,other):
        C = MaTran(self.n, other.m)
        for i in range(self.n):
            Hang = []
            for j in range(other.m):
                x = 0
                for k in range(self.m):
                    x += self.A[i][k] * other.A[k][j]
                Hang.append(x)
            C.A.append(Hang)
        return C

A = MaTran() ; B = MaTran()
A.nhap()
B.nhap()
A.xuat()
B.xuat()
if (A.congduoc(B)):
    C = A+B
    C.xuat()
if (A.nhanduoc(B)):
    C = A*B
    C.xuat()

