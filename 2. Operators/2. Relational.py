a=10
b=90
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a!=b)

a1='A'
a2='V'
print('==== Relational operators for string====')
print(a1>a2)

t='hello'
y='hi'
print(t>y)
print(t<y)
print(t<=y)
print(t>=y)

print('===same string')
t='hello'
y='hello'
print(t>y)
print(t<y)
print(t<=y)
print(t>=y)

print('===same string with one letter as caps')
t='Hello'
y='hello'
print(t>y)
print(t<y)
print(t<=y)
print(t>=y)


#Relational operators for Bool , then corresponding int values will be considered
print('Relation ops fr bool========')
q=True
w=False
print(q>w)
print(q<w)
print(q<=w)
print(q>=w)


# relational operator chaining
print('===rel op chaining====')
print(10<20<30<90)
print(10<20<80>90)
