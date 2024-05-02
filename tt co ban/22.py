def la_so_nguyen_to(n):
    # Hàm kiểm tra xem một số có phải là số nguyên tố không
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def F(N):
    # Hàm tính giá trị của F(N)
    if la_so_nguyen_to(N):
        return N
    else:
        return 0

def main():
    L = int(input("Nhập L: "))
    R = int(input("Nhập R: "))
    
    print("Giá trị của tổng F(i) * F(j) với j > i trong khoảng [L, R]:")
    total = 0
    for i in range(L, R):
        for j in range(i+1, R+1):
            total += F(i) * F(j)
    print(total)

if __name__ == "__main__":
    main()
