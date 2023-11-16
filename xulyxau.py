# Chữ hoa chữ thường
# while True:
    # try:
    #     s = input()
    #     demh = demt = 0
    #     for i in range(len(s)):
    #         if s[i]>='a' and s[i]<='z': demt += 1
    #         elif s[i]>='A' and s[i]<='Z': demh += 1

    #     if demh > demt: print(s.upper())
    #     elif demt > demh or demh == demt: print(s.lower())
    # except:
    #     break


# Xâu camelCase
# oke = True
# while oke:
#     try:
#         s = input()
#         if s=='':break
#         dem = 1
#         for i in range(len(s)):
#             if s[i]>='A' and s[i]<='Z':
#                 dem += 1
#         print(dem)
#     except:
#         break


# Xoay trái xâu
# n = int(input())
# s = input()
# n %= len(s)
# gan = ''
# for i in range(len(s)):
#     if i>=n:
#         gan += s[i]
# for i in range(len(s)):
#     if i < n:
#         gan += s[i]
# print(gan)

# Nối chuỗi
# s = input()
# s1 = input()
# print(len(s),len(s1))
# print(s+' '+s1)

# Xâu đối xứng
# s = input()
# dem = 0
# for i in range(len(s)//2):
#     if s[i] != s[len(s)-1-i]:
#         dem += 1
# print(dem)

# Xâu đối xứng 




# Chuẩn hóa ký tự trắng
# oke = True
# while oke:
#     try:
#         s = input().strip()
#         gan = s.split()
#         for i in gan:
#             print(i,end=' ')
#         print()
#     except:
#         break

# Số ký tự phân biệt
# s = input().lower()
# a = {}
# for i in s:
#     if i>='a' and i<='z':
#         a[i] = 0
# print(len(a))

# Xâu có kỹ tự khác nhau
# s = input().strip()
# n = len(s)
# dem = 0
# for i in range(0,n-1):
#     for j in range(i+1,n):
#         if s[i] == s[j]:
#             dem += 1
# if dem==0:
#     print('Yes')
# else:
#     print('No')

# Thống kê nguyên 
# lowg = True
# while lowg:
#     try:
#         s = input()
#         dem = 0
#         a = ['a','o','y','i','e','u','A','O','Y','I','E','U']
#         for i in range(len(s)):
#             if s[i] in a:
#                 dem += 1
#         print(dem)
#     except:
#         break
    
# Xâu pangram
#        HỌC THUẬT CỦA ANH NoLegs :)))
# lowg = True
# while lowg:
#     try:
#         s = input().lower()
#         a = {}
#         for i in s:
#             if i >= 'a' and i <= 'z':
#                 a[i] = 0
#         if len(a)==26:
#             print('Yes')
#         else:
#             print('No')
#     except:
#         break

# Tần suất xuất hiện của ký tự
s = input()
a = {}
for i in s:
    if i.isalpha() or i.isdigit():
        if i not in a:
            a[i] = 1
        else:
            a[i] += 1
for i in a:
    print(i+':'+str(a[i]))




