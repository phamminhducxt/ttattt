def la_so_nguyen_to(n):
    # Hàm kiểm tra xem một số có phải là số nguyên tố không
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def tim_so_nguyen_to_3_chu_so():
    # Hàm tìm số nguyên tố có ba chữ số sao cho số đó là lập phương của một số tự nhiên khi đảo ngược thứ tự các chữ số
    for num in range(100, 1000):  # Duyệt qua tất cả các số có ba chữ số
        if la_so_nguyen_to(num):  # Nếu số đó là số nguyên tố
            reverse_num = int(str(num)[::-1])  # Lấy số đảo ngược của num
            cube_root = round(reverse_num ** (1/3))  # Tính căn bậc ba của số đảo ngược
            if cube_root ** 3 == reverse_num:  # Nếu số đảo ngược là lập phương của một số tự nhiên
                return num  # Trả về số nguyên tố có ba chữ số thỏa mãn điều kiện
    return None  # Nếu không tìm thấy, trả về None

def main():
    so_nguyen_to = tim_so_nguyen_to_3_chu_so()  # Tìm số nguyên tố có ba chữ số thỏa mãn điều kiện
    if so_nguyen_to:
        print(f"Số nguyên tố có ba chữ số và là lập phương của một số tự nhiên là: {so_nguyen_to}")
    else:
        print("Không tìm thấy số nguyên tố có ba chữ số và là lập phương của một số tự nhiên")

if __name__ == "__main__":
    main()
