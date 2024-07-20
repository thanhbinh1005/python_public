n = int(input('nhập số nguyên n: '))
print('số hoàn hảo từ 1 đến',n,'là')
for i in range(1,n+1):
    dem = 0
    for j in range(1,i):
        if(i % j == 0):
            dem = dem + j
    if(dem == i):
        print(i,end=' ')