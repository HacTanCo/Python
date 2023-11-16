# Nhập và in ma trận 1 chiều
# n = int(input())
# a = []
# for i in range(n):
#     a.append(int(input()))
# for i in range(n):
#     print(a[i],end=" ")




# Nhập và in mảng 2 chiều
# Cách 1:
# n,m = map(int,input().split())
# a = []
# for i in range(n):
#     x = list(map(int,input().split()))
#     a.append(x) 
# for i in range(n):
#     for j in range(m):
#         print(a[i][j],end=" ")
#     print()
# Cách 2:
# n,m = map(int,input().split())
# a = [list(map(int,input().split())) for i in range(n)]
# for i in range(n):
#     for j in range(m):
#         print(a[i][j],end=" ")
#     print()


# Câu1:
s = input()
for i in range(len(s)):
    if s[i].isalpha():
        print(s[i],end="")
# Câu 2:
def layten(s):
    return s.split()[-1]

a = []
while True:
    name = input("Nhap hvt: ")
    if name == '':
        break
    a.append(name)

dem = 0
for i in a:
    if "Anh".lower() in layten(i).lower():
        dem += 1
print("Có %d thằng tên Anh!!!" % dem)

# Câu 3:
s = input()
gan = s[0]
index = 0
for i in range(len(s)):
    if s[i]==' ':
        index = i
for i in range(len(s)):
    if s[i]==' ' and i<index:
        gan += s[i+1]
for i in range(len(s)):
    if i>index:
        gan += s[i]
print(gan.lower()+'@huscemail.edu.vn')

# Câu 4:
try:
    s = input()
    dem = 0
    check = False
    for i in range(len(s)):
        if s[i].isdigit():
            if check==False:
                dem += 1
            check = True
        else:
            check = False
    print(dem)
except:
    print(0)