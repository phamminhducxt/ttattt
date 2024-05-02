def la_so_nguyen_to(n):
    # Hàm kiểm tra xem một số có phải là số nguyên tố không
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def tim_so_nguyen_to_theo_bieu_thuc(A, B, C, m, l):
    # Hàm tìm các số nguyên dương trong khoảng [m, l] sao cho giá trị của biểu thức Ax^2 + Bx + C là một số nguyên tố
    for x in range(m, l + 1):
        gia_tri = A * x**2 + B * x + C
        if la_so_nguyen_to(gia_tri):
            print(x)

def main():
    A = int(input("Nhập A: "))
    B = int(input("Nhập B: "))
    C = int(input("Nhập C: "))
    m = int(input("Nhập m: "))
    l = int(input("Nhập l: "))
    
    print(f"Các số nguyên dương nằm trong khoảng [{m}, {l}] sao cho giá trị của biểu thức Ax^2 + Bx + C là một số nguyên tố:")
    tim_so_nguyen_to_theo_bieu_thuc(A, B, C, m, l)

if __name__ == "__main__":
    main()
