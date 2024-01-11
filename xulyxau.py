n = int(input())
a = []
for i in range(n):
    x = list(map(int,input().split()))
    a.append(x) 
x = int(input('Nhập đỉnh cần tìm đỉnh kề: '))
print('Các đỉnh kề của '+str(x)+' !!!')
for i in range(n):
    if a[x-1][i] == 1:
        print(i+1,end=',')