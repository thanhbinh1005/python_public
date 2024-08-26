def sohoanhao(num):
    return sum(int(digit) for digit in str(num)) == 10

def timsohoanhao(k):
    count = 0
    num = 1
    while True:
        if sohoanhao(num):
            count += 1
            if count == k: 
                return num
        num += 1

k = int(input("Nhập số k: "))
result = timsohoanhao(k)
print(f"Số hoàn hảo thứ {k} là: {result}")
