x=10
y=10
print(id(x))
print(id(y))
print(x is y)
x=11
print(id(x))

x=x+1
print(id(x))
print(x)

print(10*'=')
a=100
b=a
print(id(a))
print(id(b))
b=b+1
print(id(a))
print(id(b))

print('===========')
print('immutability of bools')
s=False
d=False
print(s is d)

print('===========')
print('immutability of strs')
s='hello'
d='hello'
print(s is d)

print('===========')
print('immutability of complex')
s2=10+20j
d2=10+20j
print(id(s2))
print(id(d2))
print(s2 is d2)

