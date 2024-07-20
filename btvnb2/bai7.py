def tong_uoc(n):
    tong = 0
    for i in range(1,n):
        if(n % i == 0):
            tong = tong + i
    return tong
n = int (input('nhập số nguyên n: '))
dem = 0
print('các cặp số Amicable')
for i in range(2,n+1):
    for j in range(i,n+1):
        if(tong_uoc(i) == j) and (tong_uoc(j) == i) and (i < j):
            print(i,j)
            dem = dem + 1
if(dem == 0): print('không có cặp số nào')
