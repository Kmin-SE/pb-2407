# Input
k = 10

# Xử lý
line = ""
x = 1
while x <= k:
    line = line + "* "
    x = x + 1

# Output
print(line)

# 0: line = ""
# 1: line = "* "
# 2: line = line + "* " = "* " + "* " = "* * "
