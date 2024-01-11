# Câu 1
# td = {}
# s = input().split()
# for i in s:
#     if i not in td:
#         td[i] = 1
#     else:
#         td[i] += 1
# for i,j in td.items():
#     print('p('+i+'): '+ str(j/len(s)*100)+'%, ',end='')


# Câu 2
n = int(input())
a = []
for i in range(n):
    while 1:
        x= list(map(int,input().split()))
        if len(x)==n: 
            break
        print('Nhập lại !!!')
    a.append(x)
dem = 0
for i in range(n):
    for j in range(n):
        if a[i][j] != a[j][i]: dem += 1   
        else: dem += 0
if dem==0:
    print('Đồ thị vô hướng')
else:
    print('Đồ thị có hướng')

# Câu 3-4
class Congnhan:
    def __init__(self,mcn='',ht='',bac=0,snlv=0,nkhd={'day':0,'month':0,'year':0}):
        self.mcn = mcn
        self.ht = ht
        self.bac = bac
        self.snlv = snlv
        self.nkhd = nkhd 
    def tienluong(self):
        if self.bac==1: return self.snlv*300000
        elif self.bac==2: return self.snlv*350000
        else: return self.snlv*400000
    def show(self):
        print('------------------------------')
        print('Mã công nhân: ',self.mcn)
        print('Họ tên: ',self.ht)
        print('Bậc: ',self.bac)
        print('Số ngày làm việc: ',self.snlv)
        print('Tiền lương: ',self.tienluong())
        print('------------------------------')
    def __gt__(self,other):
        if self.nkhd['year'] > other.nkhd['year']: return True
        elif self.nkhd['year'] == other.nkhd['year'] and self.nkhd['month'] > other.nkhd['month']: return True
        elif self.nkhd['year'] == other.nkhd['year'] and self.nkhd['month'] == other.nkhd['month'] and self.nkhd['day'] > other.nkhd['day']: return True
        else: return False

class Quanly:
    def __init__(self):
        self.a = []
        self.td = {}
    def input_ql(self):
        while 1:
            self.mcn = input('\nNhập mã công nhân: ')
            if self.mcn == '': 
                break
            self.ht = input('Nhập họ tên: ')
            self.bac = int(input('Nhập bậc: '))
            while self.bac<=0 or self.bac > 3:
                self.bac = int(input('Nhập lại bậc: '))
            self.snlv = int(input('Nhập số ngày làm việc: '))
            print('Nhập ngày ký hợp đông !!!')
            self.nkhd = {}
            self.nkhd['day'] = int(input('Nhập ngày: '))
            self.nkhd['month'] = int(input('Nhập tháng: '))
            self.nkhd['year'] = int(input('Nhập năm: ')) 
            if self.mcn not in self.td:
                self.td[self.mcn] = 1
                self.a.append(Congnhan(self.mcn,self.ht,self.bac,self.snlv,self.nkhd))
                continue
            print('\nNhập lại vì trùng mã !!!')
    def luufile(self):
        with open('C:/Users/Administrator/Desktop/HTC/Python/CNBac1.txt','w') as file:
            for i in self.a:
                if i.bac==1:
                    mcn1=i.mcn
                    ht1=i.ht
                    nkhd1=i.nkhd["day"]
                    nkhd2=i.nkhd["month"]
                    nkhd3=i.nkhd["year"]
                    snlv1=i.snlv
                    luong1=i.tienluong()
                    file.write(mcn1+","+ht1+","+str(nkhd1)+"/"+str(nkhd2)+"/"+str(nkhd3)+","+str(snlv1)+","+str(luong1)+'\n')
            file.close()

    def sorttang(self):
        for i in range(len(self.a)):
            for j in range(i+1,len(self.a)):
                if self.a[i] > self.a[j]:
                    x = Congnhan()
                    x = self.a[i]
                    self.a[i] = self.a[j]
                    self.a[j] = x
        print('Danh sách sau khi sắp xếp tăng dần theo ngày ký hợp đồng !!!')
        for i in self.a:
            i.show()

x = Quanly()
x.input_ql()
x.luufile()
x.sorttang()

    




