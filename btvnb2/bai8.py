
def C(n,k):
    if (k == 0) or (k == n): return 1
    else: return C(n-1,k) + C(n-1,k-1)
n = int(input('nhập n: '))
print('tam giác pascal có',n,'hàng là\n')
for i in range(n):
    for k in range(n-i-1):
        print(' ',end=' ')
    for j in range(i+1):
        print(C(i,j),end='   ')  
    print('\n')
