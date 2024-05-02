def la_so_nguyen_to(n):
    # Hàm kiểm tra xem một số có phải là số nguyên tố không
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def dem_so_luong_so_nguyen_to_trong_doan(A, B):
    # Hàm đếm số lượng số nguyên tố trong một đoạn [A, B]
    count = 0
    for num in range(A, B + 1):
        if la_so_nguyen_to(num):
            count += 1
    return count

def la_sieu_so_nguyen_to(X):
    # Hàm kiểm tra xem một số có phải là siêu số nguyên tố không
    so_nguyen_to_trong_doan = dem_so_luong_so_nguyen_to_trong_doan(1, X - 1)
    return la_so_nguyen_to(so_nguyen_to_trong_doan)

def dem_so_luong_sieu_so_nguyen_to_trong_khoang(A, B):
    # Hàm đếm số lượng siêu số nguyên tố trong khoảng [A, B]
    count = 0
    for X in range(A, B + 1):
        if la_sieu_so_nguyen_to(X):
            count += 1
    return count

def main():
    A = int(input("Nhập A: "))
    B = int(input("Nhập B: "))
    
    so_luong_sieu_so_nguyen_to = dem_so_luong_sieu_so_nguyen_to_trong_khoang(A, B)
    
    print(f"Số lượng siêu số nguyên tố trong khoảng [{A}, {B}]: {so_luong_sieu_so_nguyen_to}")

if __name__ == "__main__":
    main()
