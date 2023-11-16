class hocphan:
    def __init__(a):
        a.mhp = ''
        a.thp = ''
        a.stc = 0
    def fill(a):
        a.mhp = input('\nNhập mã học phần: ')
        a.thp = input('Nhập tên học phần: ')
        a.stc = int(input('Nhập số tín chỉ: '))
    def show(a):
        print('----------------------------------')
        print('Mã học phần:',a.mhp)
        print('Tên học phần:',a.thp)
        print('Số tín chỉ:',a.stc)
        print('----------------------------------')
    def __gt__(a,b):
        return a.stc > b.stc
    
class quanly:
    def __init__(a):
        a.n = 0
        a.arr = []
        a.td = {}
    def fillds(a):
        a.n = int(input('Nhap danh sach hoc phan (n <= 100): '))
        while a.n>100:
            a.n = int(input('Nhap lai: '))
        for i in range(a.n):
            x = hocphan()
            while 1:
                x.fill()
                if x.mhp not in a.td:
                    a.td[x.mhp] = 1
                    a.arr.append(x)
                    break
                elif x.mhp in a.td:
                    print('\nNhập lại mã học phần !!!')
    def stcmax3(a):
        print('\nDanh sách các học phần có số tín chỉ >= 3 !!!')
        for i in a.arr:
            if i.stc >= 3:
                i.show()
    def sorttang(a):
        print('\nSort tăng dần theo số tín chỉ !!!')
        for i in range(0,a.n-1):
            for j in range(i+1,a.n):
                if(a.arr[i]>a.arr[j]):
                    x = hocphan()
                    x = a.arr[i]
                    a.arr[i] = a.arr[j]
                    a.arr[j] = x
        for i in a.arr:
            i.show()
    def savefile(a):
        with open('HocPhanCNTT.txt','w') as file:
            for i in a.arr:
                if i.mhp[0:3].upper() == 'TIN':
                    mhp1 = i.mhp
                    thp1 = i.thp
                    stc1 = i.stc
                    file.write(mhp1 + ' ; ' + thp1 + ' ; ' + str(stc1) + '\n')
c = quanly()
c.fillds()
c.stcmax3()
c.sorttang()
c.savefile()


        