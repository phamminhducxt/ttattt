def dem_so_nguyen_to(N):
    count = 0  # Khởi tạo biến đếm số lượng số nguyên tố
    for num in range(2, N + 1):  # Duyệt qua các số từ 2 đến N
        is_prime = True  # Giả sử num là số nguyên tố
        for i in range(2, int(num ** 0.5) + 1):  # Duyệt qua các số từ 2 đến căn bậc hai của num
            if num % i == 0:  # Nếu num chia hết cho i, không phải số nguyên tố
                is_prime = False
                break
        if is_prime:  # Nếu num là số nguyên tố, tăng biến đếm lên 1
            count += 1
    return count

def main():
    N = int(input("Nhập số nguyên dương N: "))  # Nhập N từ bàn phím
    count = dem_so_nguyen_to(N)  # Đếm số số nguyên tố nhỏ hơn hoặc bằng N
    print(f"Số số nguyên tố nhỏ hơn hoặc bằng {N} là: {count}")

if __name__ == "__main__":
    main()
