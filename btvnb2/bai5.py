n = int(input('nhập số nguyên n: '))
print('số Armstrong bậc 3 từ 1 đến',n,'là')
for i in range(1,n+1):
    tong = 0
    a = i
    while(a > 0):
        tong = tong + (a%10)**3
        a = a // 10
    if(tong == i):
        print(i,end=' ')