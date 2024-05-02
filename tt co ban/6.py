def tim_uoc(n):
    uoc = []  # Khởi tạo một danh sách để lưu trữ các ước của số n
    for i in range(1, n):
        if n % i == 0:
            uoc.append(i)  # Thêm ước i vào danh sách
    return uoc

def so_than_thiet(n):
    so_than_thiet = []
    for i in range(2, n):  # Duyệt qua các số từ 2 đến n-1
        uoc_i = sum(tim_uoc(i))  # Tính tổng các ước của số i
        if uoc_i < n and sum(tim_uoc(uoc_i)) == i and uoc_i != i:  # Kiểm tra nếu i và tổng các ước của i thỏa mãn điều kiện
            so_than_thiet.append((i, uoc_i))  # Thêm cặp số thân thiết vào danh sách
    return so_than_thiet

def main():
    N = int(input("Nhập số nguyên dương N: "))  # Nhập N từ bàn phím
    so_cac_cap = so_than_thiet(N)  # Tìm các cặp số thân thiết nhỏ hơn N
    print(f"Các cặp số thân thiết nhỏ hơn {N} là:")
    for pair in so_cac_cap:  # Duyệt qua từng cặp số thân thiết và in ra
        print(pair)

if __name__ == "__main__":
    main()
