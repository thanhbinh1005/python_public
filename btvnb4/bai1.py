# Nhap xau
n = int(input())
lst = []
for i in range(n):
    lst.append(input())

# Chuyen doi xau
tpl = tuple(int(x) for x in lst)

# Tinh toan
sum = 0
for i in tpl:
    sum += i
print(sum / n)