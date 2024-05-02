def la_so_nguyen_to(n):
    # Hàm kiểm tra xem một số có phải là số nguyên tố hay không
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def so_manh_me_nho_hon_N(N):
    # Duyệt qua các số từ 2 đến N-1 để tìm số mạnh mẽ
    for num in range(2, N):
        if la_so_nguyen_to(num) and la_so_nguyen_to(num ** 2) and N % num == 0:
            return num
    return None

def main():
    N = int(input("Nhập N (N < 10000): "))
    so_manh_me = so_manh_me_nho_hon_N(N)
    if so_manh_me:
        print("Số mạnh mẽ nhỏ hơn", N, "là:", so_manh_me)
    else:
        print("Không tìm thấy số mạnh mẽ nhỏ hơn", N)

if __name__ == "__main__":
    main()
