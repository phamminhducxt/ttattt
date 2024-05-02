def la_so_nguyen_to(n):
    # Hàm kiểm tra xem một số có phải là số nguyên tố không
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def tinh_tong_so_nguyen_to_trong_khoang(A, B):
    total = 0  # Khởi tạo biến tổng
    for num in range(A, B + 1):  # Duyệt qua tất cả các số trong khoảng [A, B]
        if la_so_nguyen_to(num):  # Nếu số đó là số nguyên tố
            total += num  # Cộng số nguyên tố vào tổng
    return total  # Trả về tổng của các số nguyên tố trong khoảng [A, B]


def main():
    A = int(input("Nhập số nguyên dương A: "))  # Nhập A từ bàn phím
    B = int(input("Nhập số nguyên dương B: "))  # Nhập B từ bàn phím
    if A > B:
        print("A phải nhỏ hơn hoặc bằng B.")
        return
    print(f"Tổng của các số nguyên tố trong khoảng [{A}, {B}] là:", tinh_tong_so_nguyen_to_trong_khoang(A, B))


if __name__ == "__main__":
    main()
