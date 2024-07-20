a = [1, 2, -3, 4, -5, 6]
n = len(a)

# Duyệt mảng
# Cho i chạy từ 0 đến n-1
# Với mỗi i, print(a[i]) nếu a[i] > 0

# Cách 1: SAI
# i = 0
# while i < n and a[i] > 0:
#     print(a[i])
#     i += 1

# i = 0 => print 1
# i = 1 => print 2
# i = 2 => Dừng vòng lặp

# Cách 2
i = 0
while i < n:
    if a[i] > 0:
        print(a[i])
    i += 1

# a = [1, 2, -3, 4, -5, 6]
# n = 6
# i = 0 => print 1
# i = 1 => print 2
# i = 2 => KHÔNG print
# i = 3 => print 4
# i = 4 => KHÔNG print
# i = 5 => print 6
# i = 6 => Dừng lặp

# Cách 3
for i in range(n):
    if a[i] > 0:
        print(a[i])

# Cách 4
for element in a:
    if element > 0:
        print(element)

