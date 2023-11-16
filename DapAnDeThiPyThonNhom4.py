# Câu 1:Viết chương trình nhập vào 1 số nguyên dương n, in ra màn hình tổng các số phong phú từ 1 tới n.Biết rằng, số phong phú là các số mà tổng các ước số của sốđ ó (không kể chính nó) lớn hơn số đó. 
# Ví dụ, số 12 có tổng các ước số(không kể 12) là 1+2+3+4+6=16>12. Do đó 12 là một sốphong phú.
# input:15  output:12

def TongUocSo(num):
    t_us = 0
    for i in range(1, num):
        if num % i == 0:
            t_us += i
    return t_us

def SoPP(num):
    return TongUocSo(num) > num

n = int(input(""))
t_sopp = 0
for i in range(1, n+1):
    if SoPP(i):
        t_sopp += i
print(t_sopp)

# Câu 2:Viết chương trình nhập vào một xâu s, trong xâu này có thể chứa chữ số. Hãy viết chương trình in ra số lượng số trong xâu.
# input: 1C++2022   output:2

try:
    s = input()

    ans = 0
    i = 0
    l = len(s)

    while (i < l) :
        ok = False
        while (i < l and s[i].isdigit()):
            i += 1
            ok = True
        if (ok == True):
            ans += 1
        i += 1

    print(ans)
except:
    print(0)

# Câu 3:Viết chương trình nhập vào một danh sách gồm có n học sinh, mỗi học sinh gồm có thông tin mã học sinh, họ tên, giới tính, lớp
# a. Danh sách có bao nhiêu số nam(M), bao nhiêu nữ(F).
# b. Sắp xếp và in ra danh sách học sinh theo lớp, từ nhỏ đến lớn
# input: 5
        # hs001;Nguyen Van Linh; M;10A1
        # hs002;Nguyen Nhu Mai; F;11B1
        # hs003;Tran Lan Anh; F;10A1
        # hs004;Hoang Phi; M;11B2
        # hs005;Le Bao Anh; M;10A1
# output: 3 2 
        # hs001;Nguyen Van Linh; M;10A1
        # hs003;Tran Lan Anh; F;10A1
        # hs005;LeBao Anh; M;10A1
        # hs002;Nguyen Nhu Mai; F;11B1
        # hs004;HoangPhi; M;11B2


def count_gender(data, gender):
    count = 0
    for hs in data:
        if hs[2] == gender:
            count += 1
    return count

def sort_by_class(data):
    data.sort(key=lambda hs: hs[3])
    return data

# Nhập số lượng học sinh
n = int(input())

# Khởi tạo danh sách học sinh
students = []
for i in range(n):
    hs = input()
    students.append(tuple(hs.split(';')))

# Đếm số lượng nam và nữ
num_males = count_gender(students, 'M')
num_females = count_gender(students, 'F')
print(f"{num_males} {num_females}")

# Sắp xếp danh sách theo lớp
sorted_students = sort_by_class(students)

# In danh sách học sinh
for hs in sorted_students:
    print(';'.join(hs))

# Câu 4: Cho một ma trận gồm m dòng n cột. Một Robot di chuyển trong ma trận bắt đầu từ điểm đầu tiên (x, y). Robot có thể di chuyển theo hướng UP, DOWN, LEFT và RIGHT, một lần di chuyển là 1 ô. Hãy viết chương trình tính tổng giá trị các ô mà Robot đi qua.
# input:
        # -Dòng thứ nhất gồm m, n, x, y
        # -m dòng tiếp theo thểhiện ma trận mxn
        # -Các dòng tiếp theo thể hiện hướng di chuyển của Robot.
        # -Dòng cuối cùng “FINISH” thể hiện kết thúc di chuyển'
# output: Tổng giá trị tại các ô mà Robot đi qua.

# input: 3 3 0 0
        # 4 3 0
        # 1 0 5
        # 4 2 1
        # RIGHT
        # RIGHT
        # DOWN
        # LEFT
        # FINISH
# output: 12
def nhap(A,n):
    for i in range(n):
        B = [];
        B = list(map(int, input().split()))
        A.append(B);
n,m,x,y = map(int , input().split())
s = "";
ok = True;
A = [];
nhap(A,n)
sum = A[x][y];
while(ok):
    s = input().strip();
    s = s.upper();
    if (s == "RIGHT"): y+=1;
    elif (s == "LEFT"): y-=1;
    elif (s == "DOWN"): x+=1;
    elif (s == "UP"): x-=1;
    else:
        print(sum)
        break;
    if (x < n and x >= 0 and y >= 0 and y < m): sum += A[x][y]