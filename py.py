# def Max(a,b,c):
#     d = [a,b,c]
#     d.sort()
#     return d[-1]
# a,b,c = map(float,input('Nhập 3 số thực: ').split())
# print('\nSố lớn nhất trong 3 số thực: ',Max(a,b,c))


# def shh(n):
#     s = 0
#     for i in range(1,n):
#         if n%i==0:
#             s += i
#     if s==n: return 1
#     else: return 0

# for i in range(1,1001):
#     if shh(i):
#         print(i,end=' ')

# def Count(n):
#     dem = 0
#     while(n!=0):
#         n%10
#         n //= 10
#         dem += 1
#     return dem
# n = int(input())
# print(Count(n))

# s = input()
# dem = 0
# for i in s.isdigit():
#     if s[i].isdigit():
#         dem += 1
# print(dem)

# def Ten(s):
#     return s.split()[-1]
# n = input()
# print(Ten(n))

# def Ho(s):
    # return s.split()[0]
# n = input()
# print(Ho(n))


# Cách 1:
# def Ten(s):
#     return s.split()[-1]
# def Ho(s):
#     return s.split()[0]
# def chulot(s):
#     vt = vh = 0
#     gan = ''
#     for i in range(len(s)):
#         if s[i]==' ':
#             vt = i
#     for i in range(len(s)):
#         if s[i]==' ':
#             vh = i
#             break
#     for i in range(len(s)):
#         if i>vh and i<vt:
#             gan += s[i]
#     return gan

# s = input()
# print('Họ: ',Ho(s),',','Chữ Lót: ',Chulot(s),',','Tên: ',Ten(s))

# Cách 2:
# A = list(map(str,input().split()))
# for i in range (0,len(A)):
#     if (i == 0):
#         print("Họ:" + A[0] ,end=', ')
#         print("Chữ đệm: ",end='')
#     elif (i < len(A) - 1):
#         print(A[i],end=' ')
#     else:
#         print(', ', end='')
#         print("Tên: " + A[i])


# def dao(s):
#     return s[::-1]
# n = input()
# print(dao(n))


# def MsH(n):
#     gan = ''
#     while n!=0:
#         gan += str(n%2)
#         n //= 2
#     return gan
# n = int(input())
# print(MsH(n)[::-1])

# s = input()
# gan = ''
# for i in range(len(s)):
#     if s[i]=='0' or s[i]=='1':
#         print('1')
#     else:
#         print('!') 
#         break

# Tần suất xuất hiện của ký tự
# s = input()
# x = sorted(s)
# a = {}
# for i in x:
#     if i.isalpha():
#         if i not in a:
#             a[i] = 1
#         else:
#             a[i] += 1
# for i in a:
#     print(i+'='+str(a[i]))

def check(s):
    dem = 0
    for i in range(len(s)):
        if s[i]=='0' or s[i]=='1':
            dem += 0
        else:
            dem += 1
    if dem == 0: return 1
    else: return 0
s= input()
if check(s)==1:
    x = int(s)
    sum = i = 0
    while x!=0:
        x % 10
        sum += (x%10) * 2**i
        x //= 10
        i += 1
    print(str(sum))    
