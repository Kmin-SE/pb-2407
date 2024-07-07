# Nhập năm sinh (year), chiều cao (height), cân nặng (weight)
year = int(input("Nhap nam sinh: "))
height = float(input("Nhap chieu cao: "))
weight = float(input("Nhap can nang: "))

# Tính tuổi (age)
age = 2024 - year

# BMI = weight / (height ** 2)
# print(BMI)

# if BMI < 18.5:
#     print("Gầy")
# else:
#     if BMI >= 18.5 and BMI < 25:
#         print("Bình thường")
#     else:
#         if BMI >= 25 and BMI < 30:
#             print("Thừa cân")
#         else:
#             print("Béo phì")
                
# Cách 2
# if BMI < 18.5:
#     print("Gầy")
# else:
#     if BMI < 25:
#         print("Bình thường")
#     else:
#         if BMI < 30:
#             print("Thừa cân")
#         else:
#             print("Béo phì")

# Cách sai
# if BMI < 18.5:
#     print("Gầy")

# if BMI < 25:
#     print("Bình thường")

# if BMI < 30:
#     print("Thừa cân")

# if BMI >= 30:        
#     print("Béo phì")

# Cách 3 - Chậm
# if BMI < 18.5:
#     print("Gầy")

# if BMI >= 18.5 and BMI < 25:
#     print("Bình thường")

# if BMI >= 25 and BMI < 30:
#     print("Thừa cân")

# if BMI >= 30:        
#     print("Béo phì")

# Cách 4
# if BMI < 18.5:
#     print("Gầy")
# elif BMI < 25:
#     print("Bình thường")
# elif BMI < 30:
#     print("Thừa cân")
# else:
#     print("Béo phì")

if age >= 18:
    # BMI
    BMI = weight / (height ** 2)
    print(BMI)
    if BMI < 18.5:
        print("Gầy")
    elif BMI < 25:
        print("Bình thường")
    elif BMI < 30:
        print("Thừa cân")
    else:
        print("Béo phì")
else:
    print("Khong kha dung.")

# Nếu age >= 18, thì
#   - Tính BMI = cân nặng (kg) / (chiều cao (m))^2
#   Nếu BMI < 18.5: Gầy
#   Ngược lại, Nếu BMI >= 18.5 and BMI < 25: Bình thường
#   Ngược lại, Nếu BMI >= 25 and BMI < 30: Thừa cân
#   Ngược lại, Nếu BMI > 30: Béo phì
# Ngược lại thì thông báo "Không khả dụng"

