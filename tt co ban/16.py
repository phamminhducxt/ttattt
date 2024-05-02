import random

def la_so_nguyen_to(n):
    # Hàm kiểm tra xem một số có phải là số nguyên tố không
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def tim_so_nguyen_to_trong_mang(N):
    # Hàm tạo một mảng sinh ngẫu nhiên chứa các số nguyên tố
    mang_ngau_nhien = []
    while len(mang_ngau_nhien) < N:  # Lặp cho đến khi mảng đủ kích thước
        num = random.randint(2, 1000)  # Sinh một số ngẫu nhiên trong khoảng từ 2 đến 1000
        if la_so_nguyen_to(num) and num not in mang_ngau_nhien:  # Nếu số đó là số nguyên tố và chưa có trong mảng
            mang_ngau_nhien.append(num)  # Thêm số đó vào mảng
    return mang_ngau_nhien

def main():
    N = int(input("Nhập số nguyên dương N: "))  # Nhập N từ bàn phím
    mang_nguyen_to = tim_so_nguyen_to_trong_mang(N)  # Tìm các số nguyên tố trong mảng
    print("Các số nguyên tố từ mảng sinh ngẫu nhiên:")
    print(mang_nguyen_to)

if __name__ == "__main__":
    main()
