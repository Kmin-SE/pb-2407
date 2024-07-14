m = 4
n = 8

dem = 0
for i in range(m, n+1):
    dem += 1

print(dem)

# Cách 2
dem = 0
i = m
while i <= n:
    dem = dem + 1
    i = i + 1
print(dem)