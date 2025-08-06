# int()
# float()
# complex()
# bool()
# str()

#others to int conversions
a=10.05
b=10+56j
c=True
d='12'
e='Q'
print(int(a))
#print(int(b)) since int since complex can not be converted into complex
print(int(c))
print(int(d))
#print(int(e)) since its not integer 
 
print(10*'#')
#othes to float conversion
print('others to float conversion')
print(float(10))
#print(float(10+20j))
print(float(True))
print(float('17'))
print(float(19.90))
#print(float('0xFACE')) # not possible as string need to be integeral and with base 10

#others to complex conversions
print('others to complex conversion')
print(complex(10+0j))
print(complex(0xBA12+0j))
print(complex(10.5))
print(complex(True))
print(complex(False))
print(complex('10'))
print(complex('10.9'))
#print(complex('0xFACE')) #invallid since str must be integral and base of 10
print(complex(10,20))
print(complex(10.2,90.8))
#print(complex('230',9))


#bool conversions
print('others to bool conversion')
print(bool(10))
print(bool(1))
print(bool(0))
print(bool(-10))
print(bool(10.1))
print(bool(0.000000001))
print(bool(0+0j))
print(bool(0+0.1j))
print(bool('False'))
print(bool('YES'))
print(bool(''))

#str conversions
print('others to str conversion')
print(str(10))
print(str(10.5))
print(str(10+90j))
print(str(0b1000))
print(str(True))
