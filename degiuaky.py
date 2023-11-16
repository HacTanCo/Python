from math import *
# Câu 1:
# n = int(input())
# s = 0
# for i in range(1,n):
#     if n%i==0:
#         s += i
# print(s)

# Câu 2:
# def kc(x1,y1,x2,y2):
#     return sqrt(pow(x1-x2,2) + pow(y1-y2,2))
# x1,y1,x2,y2 = map(int,input().split())
# print(kc(x1,y1,x2,y2))

# Câu 3:
# n = int(input('Nhập N: '))
# a = list(map(int,input().split()))
# x = int(input('Nhập X: '))
# dem = 0
# for i in range(n):
#     if a[i]==x:
#         dem += 1
# print(dem)
# max = vt = 0
# for i in range(n):
#     if max<a[i]:
#         max = a[i]
#         vt = i
# print('Max = ',max)
# print('Vị trí: ',vt)
# a.sort()
# print('Danh sach tang dan: ',end='')
# for i in range(n):
#     print(a[i],end=' ')

# Câu 4:
# s = input()
# sum = 0
# for i in range(len(s)):
#     if s[i].isdigit():
#         sum += int(s[i])
# print(sum)

# Câu 5.1: số từ dài nhất của xâu
# s = input()
# dem = c = 0
# for i in range(len(s)):
#     if s[i] != ' ':
#         c += 1
# #   Cách 1: để kiểm tra từ cuối cùng của xâu
# #    if s[i] == ' ' or i==len(s)-1:
#     else:
#         if dem < c:
#             dem = c
#         c = 0
# #   Cách 2: để kiểm tra từ cuối cùng của xâu
# if dem < c: dem = c
# print(dem,end=' ')        

# Câu 5.2: từ dài nhất trong xâu
a = list(map(str,input().split()))
max = 0
for i in a:
    if max < len(i):
        max = len(i)
for i in a:
    if len(i)==max:
        print(i)
        print(len(a))

# A = list(map(str,input().split()))
# mx = 0
# for i in A:
#     if (len(i) > mx): mx = len(i)
# for i in A:
#     if (len(i) == mx): print(i)
# print(len(A))

