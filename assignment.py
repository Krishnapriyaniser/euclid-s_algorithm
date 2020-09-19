#Euclids extented algorithm
n1=int(input('Enter a number:'))
n2=int(input('Enter a number:'))
l=[n1,n2]
n=max(l)
p=min(l)
x0=0
x_pre=1
y0=1
y_pre=0

while n%p != 0:
    q=n//p
    N=n
    P=p
    X0=x0
    Y0=y0
    XP=x_pre
    YP=y_pre
    n=P
    p=N-q*P
    x_pre=X0
    x0=XP-q*X0
    y_pre=Y0
    y0=YP-q*Y0
  

print ('GCD(n1,n2) is '+str(p)+'\nIt can also be written as:\n' + str(p) + "=" + str(max(l)) + '*' + str(x0) + "+" + str(min(l)) + '*' + str(y0))



