arr = [1, 3, 7, 2, 5, 9, 8, 5]

n = len(arr)
if n % 2 == 1: # SLPT là lẻ
    print(arr[n // 2])
else:
    left = arr[n//2 - 1]
    right = arr[n//2]
    print((left + right) / 2)