def la_so_nguyen_to(n):
    # Hàm kiểm tra xem một số có phải là số nguyên tố không
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def tinh_tong_so_nguyen_to(N):
    total = 0  # Khởi tạo biến tổng
    for num in range(2, N + 1):  # Duyệt qua tất cả các số từ 2 đến N
        if la_so_nguyen_to(num):  # Nếu số đó là số nguyên tố
            total += num  # Cộng số nguyên tố vào tổng
    return total  # Trả về tổng của các số nguyên tố nhỏ hơn hoặc bằng N

def main():
    N = int(input("Nhập số nguyên dương N: "))  # Nhập N từ bàn phím
    tong = tinh_tong_so_nguyen_to(N)  # Tính tổng của các số nguyên tố nhỏ hơn hoặc bằng N
    print(f"Tổng của các số nguyên tố nhỏ hơn hoặc bằng {N} là: {tong}")

if __name__ == "__main__":
    main()
