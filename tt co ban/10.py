def dem_uoc(N):
    count = 0
    for i in range(1, N + 1):  # Duyệt qua tất cả các số từ 1 đến N
        if N % i == 0:  # Nếu i là ước của N
            count += 1  # Tăng số lượng ước lên 1
    return count

def la_so_nguyen_to(n):
    # Hàm kiểm tra xem một số có phải là số nguyên tố không
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def dem_uoc_nguyen_to(N):
    count = 0
    for i in range(1, N + 1):  # Duyệt qua tất cả các số từ 1 đến N
        if N % i == 0 and la_so_nguyen_to(i):  # Nếu i là ước của N và là số nguyên tố
            count += 1  # Tăng số lượng ước nguyên tố lên 1
    return count

def main():
    N = int(input("Nhập số nguyên dương N: "))  # Nhập N từ bàn phím
    uoc = dem_uoc(N)  # Đếm số ước của N
    uoc_nguyen_to = dem_uoc_nguyen_to(N)  # Đếm số ước nguyên tố của N
    print(f"Số ước của {N} là: {uoc}")
    print(f"Số ước nguyên tố của {N} là: {uoc_nguyen_to}")

if __name__ == "__main__":
    main()
