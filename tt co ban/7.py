def la_so_nguyen_to(n):
    # Hàm kiểm tra xem một số có phải là số nguyên tố không
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def dao_nguoc_so(n):
    # Hàm đảo ngược số
    return int(str(n)[::-1])

def liet_ke_emirp(N):
    emirps = []  # Danh sách để lưu trữ các số emirp
    for num in range(2, N):
        if la_so_nguyen_to(num):  # Nếu số đó là số nguyên tố
            reversed_num = dao_nguoc_so(num)  # Đảo ngược số
            if num != reversed_num and la_so_nguyen_to(reversed_num):  # Kiểm tra xem số đảo ngược cũng là số nguyên tố và khác với số gốc
                emirps.append(num)  # Thêm số vào danh sách emirp
    return emirps

def main():
    N = int(input("Nhập số nguyên dương N: "))  # Nhập N từ bàn phím
    emirps = liet_ke_emirp(N)  # Liệt kê các số emirp nhỏ hơn N
    print(f"Các số emirp nhỏ hơn {N} là:")
    for emirp in emirps:  # Duyệt qua danh sách các số emirp và in ra
        print(emirp, end=" ")

if __name__ == "__main__":
    main()
