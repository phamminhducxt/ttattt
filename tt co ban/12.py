def la_so_nguyen_to(n):
    # Hàm kiểm tra xem một số có phải là số nguyên tố không
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def tim_so_nguyen_to_lien_tiep(N):
    # Hàm tìm bốn số nguyên tố liên tiếp sao cho tổng của chúng là số nguyên tố nhỏ hơn hoặc bằng N
    for i in range(2, N - 3):  # Duyệt qua các số từ 2 đến N - 3
        if la_so_nguyen_to(i) and la_so_nguyen_to(i + 1) and la_so_nguyen_to(i + 2) and la_so_nguyen_to(i + 3):
            # Nếu bốn số liên tiếp là số nguyên tố
            tong = i + (i + 1) + (i + 2) + (i + 3)
            if tong <= N:  # Nếu tổng của bốn số nguyên tố đó nhỏ hơn hoặc bằng N
                return (i, i + 1, i + 2, i + 3)  # Trả về bốn số nguyên tố đó
    return None  # Nếu không tìm thấy, trả về None

def main():
    N = int(input("Nhập số nguyên dương N: "))  # Nhập N từ bàn phím
    bo_n_so = tim_so_nguyen_to_lien_tiep(N)  # Tìm bốn số nguyên tố liên tiếp
    if bo_n_so:
        print(f"Bốn số nguyên tố liên tiếp nhỏ hơn hoặc bằng {N} là:", bo_n_so)
    else:
        print(f"Không tìm thấy bốn số nguyên tố liên tiếp nhỏ hơn hoặc bằng {N}")

if __name__ == "__main__":
    main()
