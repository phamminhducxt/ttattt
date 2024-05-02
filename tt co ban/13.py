def la_so_nguyen_to(n):
    # Hàm kiểm tra xem một số có phải là số nguyên tố không
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def tim_hai_so_nguyen_to(N):
    # Hàm tìm hai số nguyên tố nhỏ hơn hoặc bằng N sao cho tổng và hiệu của chúng đều là số nguyên tố
    for i in range(2, N):  # Duyệt qua tất cả các số từ 2 đến N
        if la_so_nguyen_to(i):  # Nếu i là số nguyên tố
            for j in range(i + 1, N):  # Duyệt qua các số từ i + 1 đến N
                if la_so_nguyen_to(j):  # Nếu j là số nguyên tố
                    tong = i + j
                    hieu = abs(i - j)
                    if la_so_nguyen_to(tong) and la_so_nguyen_to(hieu):  # Nếu tổng và hiệu của i và j đều là số nguyên tố
                        return (i, j)  # Trả về hai số nguyên tố đó
    return None  # Nếu không tìm thấy, trả về None

def main():
    N = int(input("Nhập số nguyên dương N: "))  # Nhập N từ bàn phím
    hai_so = tim_hai_so_nguyen_to(N)  # Tìm hai số nguyên tố nhỏ hơn hoặc bằng N
    if hai_so:
        print(f"Hai số nguyên tố nhỏ hơn hoặc bằng {N} sao cho tổng và hiệu của chúng đều là số nguyên tố là:", hai_so)
    else:
        print(f"Không tìm thấy hai số nguyên tố nhỏ hơn hoặc bằng {N} sao cho tổng và hiệu của chúng đều là số nguyên tố")

if __name__ == "__main__":
    main()
