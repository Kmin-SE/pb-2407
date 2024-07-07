# Nhập 3 cạnh vào 3 biến a, b, c
a = float(input("Nhap canh a: "))
b = float(input("Nhap canh b: "))
c = float(input("Nhap canh c: "))

# Nếu 3 cạnh bằng nhau (a == b and b == c) thì Đều, ngc lại thì Ko đều
# if a == b and b == c:
#     print("Tam giac deu")
# else:
#     print("Tam giac khong deu")

# Cách 2
# if not (a == b and b == c):
#     print("Khong phai Tam giac deu")
# else:
#     print("Tam giac deu")

# Cách 3
# if not (a == b and b == c):
#     print("Khong phai Tam giac deu")
# else:
#     print("Tam giac deu")

# Cách 4
if a != b or b != c:
    print("Khong phai Tam giac deu")
else:
    print("Tam giac deu")

# 10 5 5
# 5 5 10
# 5 10 5


# not (a < 0) => a >= 0
# not (a == b and b == c) => not(a == b) or not(b == c) => a != b or b != c

# De Morgan:
# not (X and Y) => not(X) or not(Y)
# Hôm nay trời mưa và có người yêu thì đi học
# Khi nào thì không đi học?
# Khi (trời mưa và có người yêu) sai
# Khi trời không mưa hoặc không có người yêu thì không đi học