def la_so_nguyen_to(n):
    # Hàm kiểm tra xem một số có phải là số nguyên tố không
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def tim_so_nguyen_to_thoa_man(A, B, C):
    # Hàm tìm số nguyên dương x nhỏ nhất sao cho giá trị của biểu thức Ax^2 + Bx + C là một số nguyên tố
    x = 1
    while True:
        gia_tri = A * x**2 + B * x + C
        if la_so_nguyen_to(gia_tri):
            return x
        x += 1

def main():
    A = int(input("Nhập A: "))
    B = int(input("Nhập B: "))
    C = int(input("Nhập C: "))
    
    x = tim_so_nguyen_to_thoa_man(A, B, C)
    
    print(f"Số nguyên dương x nhỏ nhất thỏa mãn điều kiện là: {x}")

if __name__ == "__main__":
    main()
