def tim_so_T_prime(N):
    T_primes = []
    for num in range(4, N + 1):  # Duyệt qua các số từ 4 đến N
        uoc_count = 0
        for i in range(1, num + 1):  # Duyệt qua các số từ 1 đến num
            if num % i == 0:
                uoc_count += 1
                if uoc_count > 3:  # Nếu số lượng ước lớn hơn 3, không phải là số T-prime
                    break
        if uoc_count == 3:  # Nếu số lượng ước là 3, là số T-prime
            T_primes.append(num)
    return T_primes

def main():
    N = int(input("Nhập số nguyên dương N: "))  # Nhập N từ bàn phím
    T_primes = tim_so_T_prime(N)  # Tìm các số T-prime nhỏ hơn hoặc bằng N
    print(f"Các số T-prime nhỏ hơn hoặc bằng {N} là:")
    for prime in T_primes:
        print(prime, end=" ")

if __name__ == "__main__":
    main()
