# Cách 1
# a = [1, 2, 3, 4, 5, 6]
# n = len(a)
# dem = 0
# for i in range(n):
#     if a[i] % 2 == 1:
#         dem += 1
# print(dem)


# Cách 2
a = [1, 5, 3, 6, 9, 6]
n = len(a)
dem = 0
for value in a:
    if value % 2 == 1:
        dem += 1
print(dem)