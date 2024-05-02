def la_so_nguyen_to(n):
    # Hàm kiểm tra xem một số có phải là số nguyên tố không
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def main():
    N = int(input("Nhập số nguyên dương N: "))  # Nhập N từ bàn phím
    p = 0  # Khởi tạo biến p là tổng của các ước số của N
    s = 0  # Khởi tạo biến s là số ước của N
    for i in range(1, N + 1):
        if N % i == 0:  # Nếu i là ước của N
            p += i  # Cộng i vào p
            s += 1  # Tăng biến đếm số ước lên 1
    q = 0  # Khởi tạo biến q là tổng của các ước nguyên tố của N
    k = 0  # Khởi tạo biến k là số ước nguyên tố của N
    for i in range(2, N + 1):
        if N % i == 0 and la_so_nguyen_to(i):  # Nếu i là ước của N và là số nguyên tố
            q += i  # Cộng i vào q
            k += 1  # Tăng biến đếm số ước nguyên tố lên 1
    result = N + p + s - q - k  # Tính giá trị của biểu thức
    print(f"Giá trị của biểu thức N+p+s-q-k là: {result}")


if __name__ == "__main__":
    main()
