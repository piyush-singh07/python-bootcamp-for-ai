#input() func of 3.x and raw_input() of 2.x behaves similar means
#return type is always string and we need to perform type cast

#demo to check return type of input()--> its always str in 3.x
inp=input('Enter a value: ')
print('Type is : ',type(inp))
inp=input('Enter a value: ')
print('Type is : ',type(inp))
inp=input('Enter a value: ')
print('Type is : ',type(inp))
inp=input('Enter a value: ')
print('Type is : ',type(inp))
# here all the return type will be str so we will have to type cast