# E-Commerce Price Filter

prices = [15000, 22000, 30000, 45000, 50000, 52000, 65000, 70000]

target = int(input("Enter Target Price: "))

low = 0
high = len(prices) - 1
ans = -1

while low <= high:
    mid = (low + high) // 2

    if prices[mid] >= target:
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

if ans != -1:
    print("First Product Price =", prices[ans])
else:
    print("No Product Found")