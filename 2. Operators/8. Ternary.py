#like in java we do have ternary operator in python but syntax is different here

a=10
b=20
c= 30 if a>b else 90
print('value of c is: ',c)

#program to find min value from two given inputs
print('====program to find min value from two given inputs====')
num1=int(input('Enter first number: '))
num2=int(input('Enter second number: '))
print('minimum number from the two numers given is: ', num1 if num1<num2 else num2)

#program to find min value from three given inputs
print('====program to find min value from three given inputs====')
num1=int(input('Enter first number: '))
num2=int(input('Enter second number: '))
num3=int(input('Enter third number: '))
print('minimum number from the three numers given is: ', 
        num1 if num1<num2 and num1<num3 else num2 if num2< num3 else num3)
