n = int (input( " Nhập  số nguyên dương a = "))
m = int (input( " Nhập  số nguyên dương b = "))
p = int (input( " Nhập  số nguyên dương c = "))
t = 0
while n > 0:
    t += n % 10
    n = n // 10
print("Tổng các chữ số là:", t)

t = 0
for i in range(1,n+1) : 
    if n % i ==0 :
        t=t+i
print ("Tổng các ước của ",n,"là : ",t)

if n+m >= p and m+p >= n and p+n>=m :
    print ("3 cạnh trên có tạo thành 1 tam giác ")
    if(m==n==p) :
        print ("Tam giác đều")
    if(n==m or n==p or m==p) :
        print ("Tam giác cân")
    if(n**2+m**2==p**2 or m**2+p**2==n**2 or n**2+p**2==m**2 ):
        print ("Tam giác vuông")
    if(n**2+m**2>p**2 and m**2+p**2>n**2 and n**2+p**2>m**2 ):
        print ("Tam giác nhọn")
    tang = sorted ([n,m,p])
    if( tang[0]**2 + tang[1]**2 < tang[2]**2) : 
        print ("Tam giác tù")
else :
    print ("3 cạnh trên không tạo thành 1 tam giác")
