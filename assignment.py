#Euclids algorithm and Euclids extented algorithm
n1=int(input('Enter a number:'))
n2=int(input('Enter a number:'))
print("Euclid's algorithm: If a=bq+r, then gcd(a,b) = gcd(b,r)")
print("If gcd(a,b)=d, then there exist integers x0 and y0 such that d=a*x0+b*y0 (Bezout's identity) ")
l=[n1,n2]
n=max(l)
p=min(l)
x0=0
x_pre=1 
y0=1
y_pre=0

if n1==0 and n2!=0:
    print('gcd(n1,n2) is '+ str(n2) +' and ' +str(n2) +'= 0 + 1*'+str(n2))
elif n2==0 and n1!=0:
    print('gcd(n1,n2) is '+ str(n1) +' and ' +str(n1) +'= 0 + 1*'+str(n1))
elif n1==0 and n2==0:
    print('gcd cannot be defined')
else:
    while n%p != 0:
        q=n//p #quotient
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
        # Initially x_pre=1 and y_pre=o.This is to make r=a-bq in the first cycle.
    if p<0:
        #In case the entered numbers are negative
        p=-p
        x0=-x0
        y0=-y0
  

    print ('GCD(n1,n2) is '+str(p)+'\nIt can also be written as:\n' + str(p) + "=" + str(max(l)) + '*' + str(x0) + "+" + str(min(l)) + '*' + str(y0))



