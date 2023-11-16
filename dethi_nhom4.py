# Câu 1:
# def check(n):
#     sum = 0
#     for i in range(1,n):
#         if n%i==0:
#             sum += i
#     if sum > n: return 1
#     else: return 0

# n = int(input())
# sum = 0
# for i in range(1,n+1):
#     if check(i)==1:
#         sum += i
# print(sum)

# Câu 2:
# try:
#     s = input()
#     dem = 0
#     check = False
#     for i in range(len(s)):
#         if s[i].isdigit():
#             if check==False:
#                 dem += 1
#             check = True
#         else:
#             check = False
#     print(dem)
# except:
#     print(0)

# Câu 3 Cách 1:
n = int(input())
a = []
demnam = 0

for i in range(n):
    x = input().split(';')
    a.append(x)
for i in a:
    if i[-2].strip()=='M':
        demnam += 1
print(demnam,n-demnam)

def CLass(x):
    return x[-1]
a.sort(key=CLass)

# in cách 1:
# for i in a:
#     for j in i:
#         if j!=i[-1]:
#             print(j,end=';')
#         else:
#             print(j)

# in cách 2:
for i in a:
    print(';'.join(i))

# Câu 3 Cách 2(TỪ ĐIỂN):
dshs = []
n = int(input())
for i in range(n):
    ma, ten, gt, lop = input().split(";")
    hs = {"ma": ma, "ten": ten, "gt": gt, "lop": lop}
    dshs.append(hs)

dshs.sort(key=lambda hocsinh: hocsinh["lop"])

slnam = sum(1 for hs in dshs if hs["gt"] == "M")
slnu = n - slnam
print(slnam, slnu)
dshs.sort(key = lambda x: x['lop'])
for hocsinh in dshs:
    print(f"{hocsinh['ma']};{hocsinh['ten']};{hocsinh['gt']};{hocsinh['lop']}")
    


