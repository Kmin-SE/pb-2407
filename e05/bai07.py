# Cách 1: Đúng cho bài MSSV (các phần tử không trùng)

# a = [4, 2, 8, 9]
# key = 1
# n = len(a)

# for i in range(n):
#     if a[i] == key:
#         print(i)
#         break
# else:
#     print("Không tìm thấy :(")

# Cách 2: Tổng quát hơn
# a = [4, 2, 8, 2]
# key = 2
# n = len(a)
# dem = 0
# for i in range(n):
#     if a[i] == key:
#         print(i)
#         dem += 1

# if dem == 0:
#     print("Không tìm thấy :(")

# Cách 3: Tổng quát hơn (cờ hiệu)
# a = [4, 2, 8, 2]
# key = 2
# n = len(a)
# flag = 0
# for i in range(n):
#     if a[i] == key:
#         print(i)
#         flag = 1

# if flag == 0:
#     print("Không tìm thấy :(")

# Cách 4 (tuyệt chiêu Python)
a = [4, 2, 8, 2]
key = 9
n = len(a)
for i in range(n):
    if a[i] == key:
        print(i)

if key not in a:
    print("Không tìm thấy :(")