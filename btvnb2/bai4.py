n = int (input( "Nhập n = "))
fib = []
a, b = 0, 1
for _ in range(n) :
    fib.append(a)
    a, b = b, a+b
print ("Dãy là : ", fib)