def la_so_nguyen_to(n):
    # Hàm kiểm tra xem một số có phải là số nguyên tố không
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def phan_tich_N_thanh_tong_M_so_nguyen_to(N, M):
    # Duyệt qua các số nguyên tố để tìm M số thỏa mãn điều kiện
    primes = []
    current_number = 2
    while len(primes) < M and current_number < N:
        if la_so_nguyen_to(current_number):
            primes.append(current_number)
        current_number += 1

    if sum(primes) == N and len(primes) == M:
        print("Có thể phân tích số", N, "thành tổng của", M, "số nguyên tố là:", primes)
    else:
        print("Không thể phân tích số", N, "thành tổng của", M, "số nguyên tố")

def main():
    N = int(input("Nhập N (1 <= N <= 10000): "))
    M = int(input("Nhập M (2 < M <= 100): "))
    
    phan_tich_N_thanh_tong_M_so_nguyen_to(N, M)

if __name__ == "__main__":
    main()
