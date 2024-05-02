def USCLN(a, b):
    # Hàm tính ước số chung lớn nhất của hai số a và b
    while b:
        a, b = b, a % b
    return a

def in_cac_cap_so(M, N, D):
    # Hàm in ra các cặp số (A, B) nằm trong khoảng (M, N) sao cho USCLN của chúng có giá trị là D
    print(f"Các cặp số (A, B) trong khoảng ({M}, {N}) sao cho USCLN của chúng là {D} là:")
    for A in range(M, N+1):
        for B in range(A+1, N+1):
            if USCLN(A, B) == D:
                print(f"({A}, {B})")

def main():
    M = int(input("Nhập M: "))
    N = int(input("Nhập N: "))
    D = int(input("Nhập D: "))
    
    in_cac_cap_so(M, N, D)

if __name__ == "__main__":
    main()
