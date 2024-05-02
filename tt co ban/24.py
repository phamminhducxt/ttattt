def la_so_nguyen_to(n):
    # Hàm kiểm tra xem một số có phải là số nguyên tố không
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    a = int(input("Nhập a: "))
    b = int(input("Nhập b: "))

    # Tạo mảng chứa các bình phương của các số nguyên từ a đến b
    S1 = [x ** 2 for x in range(int(a ** 0.5), int(b ** 0.5) + 1)]
    S2 = [x ** 2 for x in range(int(a ** 0.5), int(b ** 0.5) + 1)]

    # Đếm số lượng các số nguyên tố thỏa mãn điều kiện
    count = 0
    for num in range(a, b + 1):
        if la_so_nguyen_to(num):
            for x in S1:
                for y in S2:
                    if x + y == num:
                        count += 1
                        break  # Sau khi tìm được một cặp x, y thỏa mãn thì không cần kiểm tra tiếp
    print("Số lượng các số nguyên tố thỏa mãn điều kiện trong khoảng [", a, ",", b, "]:", count)

if __name__ == "__main__":
    main()
