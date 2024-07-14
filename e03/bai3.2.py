# Ước của 10: 1 2 5 10
# Ước của 6: 1 2 3 6
# Ước của 9: 1 3 9
# => Nhận xét: 
# 1. Ước nhỏ nhất là 1. 
# 2. Ước lớn nhất là n
# 3. Các ước sẽ luôn nằm trong đoạn [1, n]
# 4. Nếu n chia hết cho i => i là ước của n

# Cái gì đc lặp?
# Lặp mấy lần / Lặp ntn?

n = 5
for i in range(1, n+1):
    if (n % i == 0):
        print(i)

