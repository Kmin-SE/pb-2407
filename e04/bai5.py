
def xin_chao(name, yob): # name = ten = "Bao"
    print("Xin chào, mình tên là " + name + ".")
    print("Mình sinh năm " + str(yob) + ".")
    print("Rất vui được gặp bạn.")
    # age = 2024 - yob
    # return age
    return 2024 - yob

def nhap_ten():
    ten = input("Nhap ten: ")

    while ten == "":
        print("Vui long nhap ten day du.")
        ten = input("Nhap ten: ")

    return ten

    # if ten == "":
    #     print("Vui long nhap ten day du.")
    #     return ""
    # else:
    #     return ten
    
def cn_xin_chao() :
    ten = nhap_ten()
    nam_sinh = int(input("Nhap nam sinh: "))
    tuoi = xin_chao(ten, nam_sinh)
    print(tuoi)

cn_xin_chao()
