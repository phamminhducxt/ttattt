def tong_hai_so_nguyen_lon(a, b):
    max_length = max(len(a), len(b))  # Xác định chiều dài lớn nhất của hai số
    a = a.zfill(max_length)  # Thêm số 0 vào đầu cho đủ chiều dài
    b = b.zfill(max_length)
    
    tong = []  # Danh sách lưu kết quả
    nho = 0  # Biến nhớ ban đầu
    
    for i in range(max_length - 1, -1, -1):  # Duyệt từ phải sang trái
        num_sum = int(a[i]) + int(b[i]) + nho  # Tính tổng của các chữ số
        tong.append(str(num_sum % 10))  # Lưu kết quả vào danh sách
        nho = num_sum // 10  # Cập nhật biến nhớ
        
    if nho:
        tong.append(str(nho))  # Nếu còn nhớ ở vị trí cuối cùng, thêm vào kết quả
        
    tong.reverse()  # Đảo ngược danh sách để có kết quả đúng
    
    return "".join(tong)  # Chuyển danh sách kết quả về dạng chuỗi

def main():
    a = input("Nhập số nguyên lớn thứ nhất: ")
    b = input("Nhập số nguyên lớn thứ hai: ")
    
    tong = tong_hai_so_nguyen_lon(a, b)
    
    print("Tổng của hai số nguyên lớn:")
    print("Dưới dạng mảng:", tong)
    print("Dưới dạng số nguyên:", int(tong))

if __name__ == "__main__":
    main()
