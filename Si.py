p = float(input('Enter Amount:'))
r = float(input('Enter rate:'))
t = float(input('Enter time:'))

S_I = (p*r*t)/100
C_I = p*((1+r/100)*t-1)

print('Simple interest is:%f'%(S_I))
print('Compound interest is:%f'%(C_I))
