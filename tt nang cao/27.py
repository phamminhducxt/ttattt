def ucln(a, b):
    # Hàm tìm ước chung lớn nhất của hai số
    while b != 0:
        a, b = b, a % b
    return a

def la_so_nguyen_to(n):
    # Hàm kiểm tra xem một số có phải là số nguyên tố hay không
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    print("Các cặp số (a, b) thoả mãn ước chung lớn nhất là số nguyên tố:")
    for a in range(1, 1000):
        for b in range(a + 1, 1000):
            if la_so_nguyen_to(ucln(a, b)):
                print("(", a, ",", b, ")")

if __name__ == "__main__":
    main()
