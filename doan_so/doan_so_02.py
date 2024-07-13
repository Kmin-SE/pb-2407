import random

print("Hello. Tui đang giữ một số bí mật trong [1, 100]. Hãy dự đoán để nhận về phần thương trên dưới 10 tỷ. Bạn có 3 lượt đoán.")

so_bi_mat = random.randint(1, 5)
print(so_bi_mat)

dem = 0 # Số lần sai 
diem = 0
while True:
    so_doan = int(input("Nhập số của bạn: "))

    if so_doan == so_bi_mat:
        if dem == 0:
            diem = 100
        elif dem == 1:
            diem = 50
        else:
            diem = 30
        print("Chính xác. Điểm của bạn:", diem)
        break
    else:
        dem += 1

        if dem == 3:
            print("Game Over")
            break

        if so_doan < so_bi_mat:
            print("Bạn đoán sai, số bạn của bạn nhỏ quá")
        else:
            print("Bạn đoán sai, số bạn của bạn lớn quá")
        


# so_doan = int(input("Nhập số của bạn: "))

# if so_doan == so_bi_mat:
#     print("Chính xác. Điểm của bạn:", 100)
# else:
#     if so_doan < so_bi_mat:
#         print("Bạn đoán sai, số bạn của bạn nhỏ quá")
#     else:
#         print("Bạn đoán sai, số bạn của bạn lớn quá")

#     # Đoán lượt 2
#     so_doan = int(input("Nhập số của bạn: "))

#     if so_doan == so_bi_mat:
#         print("Chính xác. Điểm của bạn:", 50)
#     else:
#         if so_doan < so_bi_mat:
#             print("Bạn đoán sai, số bạn của bạn nhỏ quá")
#         else:
#             print("Bạn đoán sai, số bạn của bạn lớn quá")
        
#         # Đoán lượt 3
#         so_doan = int(input("Nhập số của bạn: "))

#         if so_doan == so_bi_mat:
#             print("Chính xác. Điểm của bạn:", 30)
#         else:
#             print("Game over.")


# if DK1:
#     CV1
# elif DK2:
#     CV2
# else:
#     CV3

# if DK1:
#     CV1
# else:
#     if DK2:
#         CV2
#     CV3
