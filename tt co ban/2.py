def la_so_nguyen_to(n):
    if n <= 1:  # Nếu n nhỏ hơn hoặc bằng 1, không phải số nguyên tố
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Duyệt qua các số từ 2 đến căn bậc hai của n
        if n % i == 0:  # Nếu n chia hết cho i, không phải số nguyên tố
            return False
    return True  # Nếu không chia hết cho bất kỳ số nào, là số nguyên tố


def main():
    N = int(input("Nhập số chữ số N (2 <= N <= 10): "))  # Nhập N từ bàn phím
    print(f"Các số nguyên tố có {N} chữ số là:")
    for num in range(10 ** (N - 1), 10 ** N):  # Duyệt qua tất cả các số có N chữ số
        if la_so_nguyen_to(num):  # Nếu số đó là số nguyên tố
            print(num, end=" ")  # In số đó ra màn hình

if __name__ == "__main__":
    main()
