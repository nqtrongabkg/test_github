i = 1
while i < 4:
    if(i != 9):
        print(i)
    else:
        break
    i = i + 1
else: 
    print("No Break")

from random import *
a = uniform(1,10)
print("uniform: ", a)

from decimal import *
#lấy tối đa 3 ký tự cả phần nguyên và phần thập phân của Decimal
getcontext().prec = 3
print(Decimal(10) / Decimal(3))

a = complex(3,4)
print('phần thực = ', a.real)
print('phần ảo = ', a.imag)

from fractions import *
a = Fraction(1, 4)
print('Fraction: ', a)

#list
a = [1, 2, 3, 4]
print(a)
s = 'dammio'
t = list(s)
print(t)

s = 'hello dammio website'
t = s.split()
print(t)

s = 'hello-dammio-website'
t = s.split('-')
print(t)

t = ['hello', 'dammio', 'website']
delimiter = ' '
print(delimiter.join(t))

Dict = {1: 'lập', 2: 'trình', 3: 'không khó'}
print(Dict[1])
print(Dict[2])
print(Dict[3])
