# 9-a
print('9-a')
a = int(input('nhập số a: '))
dem = 0
while(a != 0):
    a = a //2
    dem = dem + 1
print('cần',dem,'bit để biểu diễn ở dạng nhị phân')
# 9-b
print('9-b')
x = 'awesome'
print('python is',x)
print(f'python is {x}')
print('python is {}'.format(x))
# 9-c
print('9-c')
import sys
print('phiên bản hiện tại là',sys.version)