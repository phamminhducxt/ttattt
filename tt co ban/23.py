def la_so_nguyen_to(n):
    # Hàm kiểm tra xem một số có phải là số nguyên tố không
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def tong_so_nguyen_to_trong_khoang(A, B):
    # Hàm tính tổng của các số nguyên tố trong khoảng từ A đến B
    total = 0
    for num in range(A, B + 1):
        if la_so_nguyen_to(num):
            total += num
    return total

def main():
    A = int(input("Nhập A: "))
    B = int(input("Nhập B: "))
    
    tong_nguyen_to = tong_so_nguyen_to_trong_khoang(A, B)
    
    if la_so_nguyen_to(tong_nguyen_to):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
