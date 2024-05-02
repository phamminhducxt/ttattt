def so_uoc(n):
    # Hàm này đếm số lượng ước của một số nguyên dương n
    count = 0  # Khởi tạo biến count để đếm số ước
    for i in range(1, n + 1):  # Duyệt qua các số từ 1 đến n
        if n % i == 0:  # Nếu n chia hết cho i
            count += 1  # Tăng biến đếm lên 1
    return count  # Trả về số lượng ước của n


def main():
    N = int(input("Nhập vào một số nguyên dương N: "))  # Nhập số nguyên dương N từ bàn phím
    print(f"Các số Q-Prime nhỏ hơn hoặc bằng {N} là:")
    for i in range(2, N + 1):  # Duyệt qua các số từ 2 đến N
        if so_uoc(i) == 4:  # Nếu số lượng ước của số i là 4
            print(i, end=" ")  # In số i ra màn hình

if __name__ == "__main__":
    main()
