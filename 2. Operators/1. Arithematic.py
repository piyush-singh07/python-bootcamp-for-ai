# This file has only the new opwerators in python like the // and **
a=10
b=2
print(a//b) # if both int then ans will be int

a1=10.0
b1=2
print(a1//b1) #since a1 is float then ans will be in float


a2=10
b2=2.0
print(a2//b2) #since a1 is float then ans will be in float

a3=100.0
b3=3
print(a3/b3)
print(a3//b3)

# ** means expo or power
print("=====Expo=====")
print(10**2) #100
print(5**3) #125


# + with string will be used for string concatenatioon but 
# both args must be string else will be getting Type Error
print("=====+ for concat=====")
print('hello'+'hi')
#print('hello'+10)  # Type Error
print('hello'+'10') 
#or
print('hello'+str(10))


# * operator can be applied with string but with one int value for repeation 
print("===== * for string repeatition=====")
print(5* ' hello')
print('Bye ' * 6)