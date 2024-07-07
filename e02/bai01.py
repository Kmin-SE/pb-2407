# Nhập x
x = int(input("Nhap x: "))

# Cách 1
# Kiểm tra: Nếu x < 0, thì in "Yes", ngc lại thì "No"
# if x < 0:
#     print("Yes")
# else:
#     print("No")

# Cách 2
# if x >= 0:
#     print("No") # Không âm
# else:
#     print("Yes")

# Cách 3
if not (x < 0):
    print("No") # Không âm
else:
    print("Yes")