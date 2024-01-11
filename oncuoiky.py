class khachhang:
    def __init__(self,mkh='',ht='',dc='',csc=0,csm=0):
        self.mkh = mkh
        self.ht = ht
        self.dc = dc
        self.csc = csc
        self.csm = csm
    def get_mkh(self):
        return self.mkh
    def ldtt(self):
        return self.csm - self.csc
    def tiendien(self):
        a = 50*1678;b = 50*1734;c = 100*2014;d = 100*2536;e = 100*2834
        if 0<self.ldtt()<=50:
            return self.ldtt()*1678
        elif 50<self.ldtt()<=100:
            return (self.ldtt()-50)*1734 + a
        elif 100<self.ldtt()<=200:
            return (self.ldtt()-100)*2014 + a + b  
        elif 200<self.ldtt()<=300:
            return (self.ldtt()-200)*2536 + a + b + c
        elif 300<self.ldtt()<=400:
            return (self.ldtt()-300)*2834 + a + b + c + d
        else:
            return (self.ldtt()-400)*2927 + a + b +c + d + e
    def input(self):
        self.mkh = input('\nNhập mã khách hàng: ')
        self.ht = input('Nhập họ tên: ')
        self.dc = input('Nhập địa chỉ: ')
        self.csc = int(input('Nhập chỉ số cũ: '))
        self.csm = int(input('Nhập chỉ số mới: '))
    def show(self):
        print('------------------------------------')
        print('Mã khách hàng:',self.mkh)
        print('Họ tên:',self.ht)
        print('Địa chỉ:',self.dc)
        print('Lượng điện tiêu thụ:',self.ldtt())
        print('------------------------------------')

class quanly:
    def __init__(self):
        self.n = 0
        self.a = []
        self.td = {}
    def input_ql(self):
        self.n = int(input('Nhập số lượng khách hàng (5-10 khách hàng): '))
        while self.n <= 0 or self.n >10:
            self.n = int(input('\nNhập lại số lượng khách hàng: '))
        for i in range(self.n):
            x = khachhang()
            while 1:
                x.input()
                if x.mkh not in self.td:
                    self.td[x.mkh] = 0
                    self.a.append(x)
                    break
                else:
                    print('\nNhập lại vì trùng mã !!!')
    
    def luufile(self):
        with open('C:/Users/Administrator/Desktop/HTC/Python/KhachHang.txt','w') as file:
            for i in self.a:
                mkh1 = i.mkh
                ht1 = i.ht
                dc1 = i.dc
                csc1 = i.csc
                csm1 = i.csm
                file.write(mkh1 + ',' + ht1 + ',' + dc1 + ',' + str(csc1) + ',' + str(csm1) + '\n')
            file.close()

    def docfile(self):
        ListKH = []
        with open('C:/Users/Administrator/Desktop/HTC/Python/KhachHang.txt','r') as file:
            for line in file:
                a = line.split(',')
                x = khachhang(a[0],a[1],a[2],int(a[3]),int(a[4]))
                if line.strip() != '':
                    ListKH.append(x)
            file.close()
        print('\nDanh sách sau khi đọc file !!!')
        for i in ListKH:
            i.show()
    def luufile50(self):
        with open('C:/Users/Administrator/Desktop/HTC/Python/KH50.txt','w') as file:
            for i in self.a:
                if i.ldtt()>50:
                    mkh1 = i.mkh
                    ht1 = i.ht
                    dc1 = i.dc
                    csc1 = i.csc
                    csm1 = i.csm
                    file.write(mkh1 + ',' + ht1 + ',' + dc1 + ',' + str(csc1) + ',' + str(csm1) + '\n')
            file.close()

    def top1(self):
        max = self.a[0]
        for i in self.a:
            if max.tiendien() < i.tiendien():
                max = i
        print('\nDanh sách khách hàng cso tiền điện sử dụng cao nhất !!!')
        for i in self.a:
            if max.tiendien()==i.tiendien():
                i.show()
    
x = quanly()
x.input_ql()
x.luufile()
x.docfile()
x.luufile50()
x.top1()

