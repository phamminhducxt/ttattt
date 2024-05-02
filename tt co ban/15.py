def la_so_nguyen_to(n):
    # Hàm kiểm tra xem một số có phải là số nguyên tố không
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def tim_so_nguyen_to_sinh_doi(N):
    # Hàm tìm các cặp số nguyên tố sinh đôi nhỏ hơn hoặc bằng N
    so_nguyen_to_sinh_doi = []
    for num in range(2, N):  # Duyệt qua các số từ 2 đến N
        if la_so_nguyen_to(num) and la_so_nguyen_to(num + 2):  # Nếu num và num + 2 đều là số nguyên tố
            so_nguyen_to_sinh_doi.append((num, num + 2))  # Thêm cặp số nguyên tố sinh đôi vào danh sách
    return so_nguyen_to_sinh_doi

def main():
    N = int(input("Nhập số nguyên dương N: "))  # Nhập N từ bàn phím
    so_nguyen_to_sinh_doi = tim_so_nguyen_to_sinh_doi(N)  # Tìm các cặp số nguyên tố sinh đôi nhỏ hơn hoặc bằng N
    if so_nguyen_to_sinh_doi:
        print(f"Các cặp số nguyên tố sinh đôi nhỏ hơn hoặc bằng {N} là:")
        for pair in so_nguyen_to_sinh_doi:
            print(pair[0], "-", pair[1])
    else:
        print(f"Không tìm thấy cặp số nguyên tố sinh đôi nhỏ hơn hoặc bằng {N}")

if __name__ == "__main__":
    main()
