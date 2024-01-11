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

from math import *
class Iris:
    def __init__(self,x1=0,x2=0,x3=0,x4=0,loai = None):
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
        # xóa khoãng trắng thừa của loại
        self.loai = self.loai.strip()
    def setkieuhoa(self,loai):
        self.loai = loai
    def kc(self,other):
        x = sqrt( (self.x1 - other.x1)**2+(self.x2 - other.x2)**2+(self.x3 - other.x3)**2+(self.x4 - other.x4)**2 )
        return round(x,2)
    def xuat(self):
        print(self.x1,self.x2,self.x3,self.x4,self.loai) 
A = []
with open("C:/Users/Administrator/Desktop/HTC/Python/iris.data", "r") as file:
    for line in file:
        x = Iris()
        if (line.strip() != ""):
            x.nhap(line)
            A.append(x)


# x1 = 7.1, x2 = 2.8, x3 = 6.4, x4 = 1.6, C = None và k = 3

X = Iris(7.1,2.8,6.3,1.6)
# sắp xếp mảng theo khoảng cách từ X đến các phần tử trong mảng
# cách 1 
# A = sorted(A,key = lambda  x:x.kc(X))
# cách 2
for i in range (0,len(A)):
    for j in range (i ,len(A)):
        if (X.kc(A[i]) > X.kc(A[j])):
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
# kc sau khi đc sắp xếp 
for i in A:
    print(X.kc(i))
# giả sử t có mảng B[3] => B[0] là cây loại 1 || B[1] cây loại 2 || B[2] cây loại 3
B = [0]*3
for i in range(3):
    if (A[i].loai== "Iris-setosa"): B[0] += 1
    elif(A[i].loai == "Iris-versicolor"): B[1] += 1
    elif(A[i].loai == "Iris-virginica"): B[2] += 1

# tìm mảng có số lớn nhất
mx = 0
loai = ""
for i in range(3):
    if (B[i] > mx ):
        mx = B[i]
        loai = i
if (loai == 0): 
    loai='Iris-setosa'
elif (loai == 1):
    loai='Iris-versicolor'
elif (loai == 2):
    loai='Iris-virginica'
X.setkieuhoa(loai)
X.xuat()