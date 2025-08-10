#Fundamental DTs have reusability concept except complex while collections dont have
x=10
y=10
print('comparison of x=10 and y=10')
print(id(x))
print(id(y))
print(x is y)
print(x is not y)
print(x==y)
print('comparison of x=hello and y=hello')
x='hello'
y='hello'
print(id(x))
print(id(y))
print(x is y)
print(x is not y)
print(x==y)
print('comparison of x=[10,20,30] and y=[10,20,30]')
x=[10,20,30]
y=[10,20,30]
print(id(x))
print(id(y))
print(x is y) #reference compare so False
print(x is not y) #True
print(x==y) #content compare


#membership operators
print('===checking membership operators===')
mystring='I love myself'
print('I' in mystring)
print('I' not in mystring)
print('d' in mystring)
print('love' in mystring)
print('===checking membership operators for list===')
l1=[10,90,20,22]
print(10 in l1)
print(100 not in l1)
print(90 not in l1)
print(90 in l1)