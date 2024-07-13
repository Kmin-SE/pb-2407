import random

print("Hello. Tui đang giữ một số bí mật trong [1, 100]. Hãy dự đoán để nhận về phần thương trên dưới 10 tỷ. Bạn có 3 lượt đoán.")

so_bi_mat = random.randint(1, 5)
print(so_bi_mat)

so_doan = int(input("Nhập số của bạn: "))

if so_doan == so_bi_mat:
    print("Chính xác. Điểm của bạn:", 100)
else:
    if so_doan < so_bi_mat:
        print("Bạn đoán sai, số bạn của bạn nhỏ quá")
    else:
        print("Bạn đoán sai, số bạn của bạn lớn quá")

    # Đoán lượt 2
    so_doan = int(input("Nhập số của bạn: "))

    if so_doan == so_bi_mat:
        print("Chính xác. Điểm của bạn:", 50)
    else:
        if so_doan < so_bi_mat:
            print("Bạn đoán sai, số bạn của bạn nhỏ quá")
        else:
            print("Bạn đoán sai, số bạn của bạn lớn quá")
        
        # Đoán lượt 3
        so_doan = int(input("Nhập số của bạn: "))

        if so_doan == so_bi_mat:
            print("Chính xác. Điểm của bạn:", 30)
        else:
            print("Game over.")


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
