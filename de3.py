from math import *
# Câu 1a:
# for i in range(1000,2024,1):
#     if i%2==0:
#         if i!=2022:
#             print(str(i),end=',')
#         else:
#             print(str(i),end='.')

# Câu 1b:
# a = {}
# for i in range(1,21):
#     a[i] = sqrt(i)
# for key,value in a.items():
#     print(str(key) + ' : ' + str(value))

# Câu 2:
# def check(a,b):
#     x = gcd(a,b)
#     if x == 1: return 1
#     else: return 0

# lst = list(map(int,input().split()))
# a = []
# # 2 vong for để kiểm tra
# for i in range(len(lst)):
#     for j in range(i+1, len(lst)):
#         if check(lst[i],lst[j]) == 1:
#             # if đúng thì thêm 2 giá trị lst[i] và lst[j] vào trong mảng a 
#             a.append((lst[i],lst[j]))

# if a:
#     print('Danh sach cac so nguyen to cung nhau !!!')
#     for i in a:
#         print(i[0],'va',i[1])
# else:
#     print('Khong co cap so nguyen to cung nhay trong danh sach')

# Câu 3 and 4:
class lodat:
    def __init__(a):
        a.cd = 0
        a.cr = 0
        a.loai = 0
    def fillld(a):
        a.cd = int(input('\nNhập chiều dài: '))
        a.cr = int(input('Nhập chiều rộng: '))
        a.loai = int(input('Nhập loại lô đất: '))
        while a.loai<=0 or a.loai > 3:
            a.loai = int(input('Nhập lại:'))
    def showld(a):
        print('---------------------------')
        print('Chiều dài:',a.cd)
        print('Chiều rộng:',a.cr)
        print('Đất loại:',a.loai)
        print('---------------------------')
    def cv(a):
        return (a.cd + a.cr) * 2
    def dt(a):
        return a.cd * a.cr
    def gialodat(a):
        if a.loai == 1:
            return a.dt() * 30
        if a.loai == 2:
            return a.dt() * 27
        if a.loai == 3:
            return a.dt() * 24
class quanly:
    def __init__(a):
        a.n = 0
        a.arr = []
    def fillql(a):
        a.n = int(input('Nhập số lượng lô đất: '))
        while a.n <= 0:
            a.n = int(input('Nhập lại: '))
        for i in range(a.n):
            x = lodat()
            x.fillld()
            a.arr.append(x)
        print('\nDanh sách lô đất sau khi nhập !!!')
        for i in a.arr:
            i.showld()    
    def top1andtopcuoi(a):
        max = a.arr[0]
        min = a.arr[0]
        print('\nLô đất có chu vi lớn nhất !!!')
        for i in a.arr:
            if max.cv() < i.cv():
                max = i
        for i in a.arr:
            if max.cv() == i.cv():
                i.showld()   
        print('\nLô đất có chu vi nhỏ nhất !!!')
        for i in a.arr:
            if min.cv() > i.cv():
                min = i
        for i in a.arr:
            if min.cv() == i.cv():
                i.showld() 
    def sort(a):
        for i in range(0,a.n-1):
            for j in range(i+1,a.n):
                if a.arr[i].dt() > a.arr[j].dt():
                    x = lodat()
                    x = a.arr[i]
                    a.arr[i] = a.arr[j]
                    a.arr[j] = x
        print('\nDanh sách các lô đất theo thứ tự tăng dần của diện tích !!!')
        for i in a.arr:
            i.showld()
    def gan150(a):
        a.arr.sort(key=lambda x: (x.dt() - 150))
        print('\nDanh sách các lô đất được sắp xếp theo tiêu chí gần 150m2:')
        for i in a.arr:
            i.showld()
    def lietke(a):
        print('\nDanh sách các lô đất có diện tích từ 100m2 đến 150m2 và có giá nhỏ hơn 3500 triệu đồng !!!')
        for i in a.arr:
            if 100 <= i.dt() <= 150 and i.gialodat() < 35000:
                i.showld()

x = quanly()
x.fillql()
x.top1andtopcuoi()
x.sort()
x.gan150()
x.lietke()