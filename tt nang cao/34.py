import random

def fermat_test(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    # Thực hiện kiểm tra k lần
    for _ in range(k):
        a = random.randint(2, n - 1)
        # Nếu a^(n-1) không kết thúc bằng 1, n không phải là số nguyên tố
        if pow(a, n - 1, n) != 1:
            return False
    return True

def main():
    n = int(input("Nhập số cần kiểm tra: "))
    if fermat_test(n):
        print(n, "là số nguyên tố.")
    else:
        print(n, "không phải là số nguyên tố.")

if __name__ == "__main__":
    main()
