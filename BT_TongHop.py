# Câu 1:
# def check(s):
#     dem = 0
#     for i in range(len(s)):
#         if s[i]=='0' or s[i]=='1':
#             dem += 0
#         else:
#             dem += 1
#     if dem == 0: return 1
#     else: return 0
# s= input()
# if check(s)==1:
#     x = int(s)
#     sum = i = 0
#     while x!=0:
#         sum += (x%10) * 2**i
#         x //= 10
#         i += 1
#     print(sum) 

# Câu 2:

# n = 7
# a = []
# for i in range(n):
#     while 1:
#         x = list(map(int,input().split()))
#         if len(x) == n: break
#         print('Nhập lại !!!')
#     a.append(x) 
# while 1:
#     x = int(input('Nhập đỉnh cần tìm đỉnh kề: '))
#     if x>0 and x<8: break
#     print('Nhập lại !!! ')
# print('Các đỉnh kề của '+str(x)+' !!!')
# for i in range(n):
#     if a[x-1][i] == 1:
#         print(i+1,end=' ')



# Câu 3:
class Hoanghoa:
    def __init__(self,mh='',th='',sl=0,gb=0):
        self.mh = mh
        self.th = th
        self.sl = sl
        self.gb = gb
    def set_mh(self,mh):
        self.mh = mh
    def get_mh(self):
        self.mh
    def set_th(self,th):
        self.th = th
    def get_th(self):
        self.th
    def set_sl(self,sl):
        self.sl = sl
    def get_sl(self):
        self.sl
    def set_gb(self,gb):
        self.gb = gb
    def get_gb(self):
        self.gb
    # def input(self):
    #     self.mh = input('\nNhập mã hàng: ')
    #     self.th = input('Nhập tên hàng: ')
    #     self.sl = int(input('Nhập số lượng: '))
    #     self.gb = int(input('Nhập giá bán: '))
    def show(self):
        print('------------------------------')
        print('Mặt hàng:',self.mh)
        print('Tên hàng:',self.th)
        print('Số lượng:',self.sl)
        print('Giá bán:',self.gb)
        print('------------------------------')
        
class Quanly:
    def __init__(self):
        self.a = []
        self.td = {}
    def input_ql(self):
        while True:
            self.mh = input('\nNhập mã hàng: ')
            if self.mh == '':
                break
            self.th = input('Nhập tên hàng: ')
            self.sl = int(input('Nhập số lượng: '))
            self.gb = int(input('Nhập giá bán: '))
            if self.mh not in self.td:
                self.td[self.mh] = 1
                self.a.append(Hoanghoa(self.mh,self.th,self.sl,self.gb))
                continue
            print('\nNhập lại vì trùng mã hàng: ')
            # for i in range(a.n):
            # x = hocphan()
            # while 1:
            #     x.fill()
            #     if x.mhp not in a.td:
            #         a.td[x.mhp] = 1
            #         a.arr.append(x)
            #         break
            #     elif x.mhp in a.td:
            #         print('\nNhập lại mã học phần !!!')
    def luufile(self):
        with open('C:/Users/Administrator/Desktop/HTC/Python/hanghoa.txt','w',encoding='utf-8') as file:
            for i in self.a:
                mh1 = i.mh
                th1 = i.th
                sl1 = i.sl
                gb1 = i.gb
                file.write(mh1 + ';' + th1 + ';' + str(sl1) + ';' + str(gb1) + '\n')
            file.close()
    def docfile(self):
        ListMH = []
        with open('C:/Users/Administrator/Desktop/HTC/Python/hanghoa.txt', 'r', encoding='utf-8') as file:
            for line in file:
                a = line.split(';')
                x = Hoanghoa(a[0],a[1],int(a[2]),int(a[3]))
                if line.strip() != '':
                    ListMH.append(x)
            file.close()
        print('\nDanh sách sau khi đọc file !!!')
        for i in ListMH:
            if i.gb > 20000:
                i.show()
                
x = Quanly()
x.input_ql()
x.luufile()
x.docfile()
#     def docfile(self):
#         # dat bien ngu v
#         a = []
#         with open('hanghoa.txt', 'r') as file:
#             for line in file:
#                 A = line.split(';')
#                 x = Hoanghoa(A[0], A[1] ,int(A[2]) ,int(A[3]))
#                 if line.strip() != '':
#                     a.append(x)
#             file.close()
#         print('\nDanh sách sau khi đọc file !!!')
#         for i in a:
#             if i.gb > 20000:
#                 i.show()

# class Hoanghoa:
#     def __init__(self, mh='', th='', sl=0, gb=0):
#         self.mh = mh
#         self.th = th
#         self.sl = sl
#         self.gb = gb

#     def set_mh(self, mh):
#         self.mh = mh

#     def get_mh(self):
#         self.mh

#     def set_th(self, th):
#         self.th = th

#     def get_th(self):
#         self.th

#     def set_sl(self, sl):
#         self.sl = sl

#     def get_sl(self):
#         self.sl

#     def set_gb(self, gb):
#         self.gb = gb

#     def get_gb(self):
#         self.gb

#     # def input(self):
#     #     self.mh = input('\nNhập mã hàng: ')
#     #     self.th = input('Nhập tên hàng: ')
#     #     self.sl = int(input('Nhập số lượng: '))
#     #     self.gb = int(input('Nhập giá bán: '))
#     def show(self):
#         print('------------------------------')
#         print('Mặt hàng:', self.mh)
#         print('Tên hàng:', self.th)
#         print('Số lượng:', self.sl)
#         print('Giá bán:', self.gb)
#         print('------------------------------')


# class Quanly:
#     def __init__(self):
#         self.a = []
#         self.td = {}

#     def input_ql(self):
#         while True:
#             self.mh = input('\nNhập mã hàng: ')
#             if self.mh == '':
#                 break
#             self.th = input('Nhập tên hàng: ')
#             self.sl = int(input('Nhập số lượng: '))
#             self.gb = int(input('Nhập giá bán: '))
#             if self.mh not in self.td:
#                 self.td[self.mh] = 1
#                 self.a.append(Hoanghoa(self.mh, self.th, self.sl, self.gb))
#                 continue
#             print('\nNhập lại vì trùng mã hàng: ')

#     def luufile(self):
#         with open('hanghoa.txt', 'w') as file:
#             for i in self.a:
#                 mh1 = i.mh
#                 th1 = i.th
#                 sl1 = i.sl
#                 gb1 = i.gb
#                 file.write(mh1 + ';' + th1 + ';' + str(sl1) + ';' + str(gb1) + '\n')
#             file.close()

#     def docfile(self):
#         # dat bien ngu v
#         a = []
#         with open('hanghoa.txt', 'r') as file:
#             for line in file:
#                 A = line.split(';')
#                 x = Hoanghoa(A[0], A[1] ,int(A[2]) ,int(A[3]))
#                 if line.strip() != '':
#                     a.append(x)
#             file.close()
#         print('\nDanh sách sau khi đọc file !!!')
#         for i in a:
#             if i.gb > 20000:
#                 i.show()


# x = Quanly()
# x.input_ql()
# x.luufile()
# x.docfile()