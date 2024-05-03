def is_coprime(a, b):
    # Hàm kiểm tra xem hai số có cùng nhau với nhau (coprime) hay không
    while b != 0:
        a, b = b, a % b
    return a == 1

def carmichael_test(n):
    # Kiểm tra xem một số có phải là số Carmichael hay không
    if n <= 2 or n % 2 == 0:  # Số Carmichael phải là số lẻ và lớn hơn 2
        return False
    for b in range(2, n):
        if is_coprime(b, n) and pow(b, n - 1, n) != 1:
            return False
    return True

def main():
    N = int(input("Nhập số N: "))
    print("Các số Carmichael nhỏ hơn", N, "là:")
    for num in range(3, N, 2):  # Bắt đầu từ 3 và chỉ xét các số lẻ
        if carmichael_test(num):
            print(num, end=" ")

if __name__ == "__main__":
    main()
