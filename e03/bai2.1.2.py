# Input
k = 3

# Chạy từ 1 đến k => range(1, k+1) => Lặp k lần
# Chạy từ 0 đến k-1 => range(0, k) => range(k) => Lặp k lần

line = ""

for i in range(k):
    line = line + "* "

print(line)
