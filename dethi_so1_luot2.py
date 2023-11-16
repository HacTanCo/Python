# Câu 1:
# s = input()
# for i in range(len(s)):
#     if s[i].isalpha():
#         print(s[i],end="")

# Câu 2:
# a = []
# while 1:
#     name = input("Nhap ten mat hang (an enter de ket thuc): ")
#     if name=="":
#         break
#     sl = int(input("Nhap so luong mat hang: "))
#     gb = int(input("Nhap gia ban mat hang: "))
#     a.append({"Ten":name, "Soluong":sl, "Giaban":gb})

# print("Cac mat hang co so luong < 5:")
# for i in a:
#     if i["Soluong"] < 5:
#         print(i)
# sum = 0  
# for i in a:
#     sum += i["Soluong"]*i["Giaban"]
# print("tong tien hang: ",sum)

# Câu 3 and 4:
# from math import *
# class Iris:
#     def __init__(a):
#         a.x1 = 0
#         a.x2 = 0
#         a.x3 = 0 
#         a.x4 = 0
#         a.c = None
#     def setKieuhoa(a,c):
#         a.c=c
#     def tinhkhoancach(a,o):
#         return round(sqrt((a.x1 - o.x1)**2 + (a.x2 - o.x2)**2 + (a.x3 - o.x3)**2 + (a.x4 - o.x4)**2),2)
#     def docfile(a):
#         a.arr = []
#         with open('C:/Users/Administrator/Desktop/HTC/Python/iris.data', 'r') as file:
#             for line in file:
#                 x = Iris()
#                 x.fi





import math
class Iris:
    def __init__(self,x1,x2,x3,x4,loai = None):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        self.loai = loai
    def nhap(self,x):
        self.x1, self.x2, self.x3, self.x4, self.loai = map(str,x.split(','))
        self.x1 = float(self.x1)
        self.x2 = float(self.x2)
        self.x3 = float(self.x3)
        self.x4 = float(self.x4)
        self.loai = self.loai.strip()
        if (self.loai == ""): self.loai = None;
    def setkieuhoa(self,loai):
        self.loai = loai
    def kc(self,other):
        x = math.sqrt( (self.x1 - other.x1)**2+(self.x2 - other.x2)**2+(self.x3 - other.x3)**2+(self.x4 - other.x4)**2 )
        return round(x,2)
    def xuat(self):
        print(self.x1,self.x2,self.x3,self.x4,self.loai)
A = [];
with open("iris.data", "r") as file:
    for line in file:
        x = Iris(1,2,3,4)
        x.nhap(line)
        A.append(x)
# x1 = 7.1, x2 = 2.8, x3 = 6.4, x4 = 1.6, C = None và k = 3
X = Iris(7.1,2.8,6.3,1.6)
A = sorted(A,key = lambda  x:x.kc(X))
mp = {"Iris-setosa": 0 ,"Iris-versicolour": 0 , "Iris-virginica": 0}
for i in range (0,min(3,len(A)) ):
    mp[A[i].loai] += 1
mx = max(mp.values())
for j,i in mp.items():
    if (i == mx): X.setkieuhoa(j)
x.xuat()