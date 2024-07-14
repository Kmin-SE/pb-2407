m = int(input('Nhập số m: '))
n = int(input('Nhập số n: '))
print("Các số chia hết cho 6 là: ")

for i in range(m, n+1):
    if i % 6 == 0:
        print(i)
        break