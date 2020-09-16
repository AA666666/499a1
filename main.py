q=int(input('type 1 if you want to do multiplication,type 2 if you want to do division:'))
n1=float(input('please type your fist number:'))
n2=float(input('please type your second number:'))
n3=float(input('please type your third number:'))

def mul(n1,n2,n3):
 n4=n1*n2*n3
 return n4


def div(n1,n2,n3):
 n5=n1/n2/n3
 return n5

if q == 1:
    print('the result of multiplication is: %s' % mul(n1,n2,n3))
elif q == 2:
    print('the result of division is: %s' % div(n1,n2,n3))
else:
    print('error')

assert mul(n1,n2,n3) == n1+n2+n3
assert div(n1,n2,n3) == n1/n2/n3

