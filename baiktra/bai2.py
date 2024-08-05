x = -1
a = 1
b = 2
c = 3

while x < 1 or x > 1000:
    x = int(input("nhập số nguyên dương x: "))
    if x > 0 and x <= 1000:
        break
d = x // c
e = (x - c*d) // b
f = (x - c*d - e*b)/a
print(f"số bước tối thiểu mà chú rùa cần để di chuyển từ điểm 0 đến điểm {x} một cách nhanh nhất : {d + e + f}")