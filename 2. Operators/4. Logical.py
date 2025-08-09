# and for bool
print('and operator')
print(True and True)
print(True and False)
print(False and False )
print(False and True)

# or for bool
print('or operator')
print(True or True)
print(True or False)
print(False or False )
print(False or True)

#not for bool
print('not operator')
print(not True)
print(not False)

# auth app
# print('===auth app===')
# uname=input('Enter username: ')
# pwd=input('Enter password :')
# if uname=='mine' and pwd=='nine':
#     print('user accepted')
# else: 
#     print('invalid user')


#Logical operator for non-bools

#concept : x and y => if x evaluates to True then result will be y
#                     if x evaluates to False then result will be x
print('Logical and operator for ')
print(10 and 20)  # 20
print(0 and 20)   # 0
print(1 and 11)   # 11
print(0 and 80)   # 0


#concept : x or y => if x evaluates to True then result will be x
#                     if x evaluates to False then result will be y
print('Logical or operator for ')
print(10 or 20)  # 10
print(0 or 20)   # 20
print(1 or 11)   # 1
print(0 or 80)   # 80
print(10 or 0) # 10
print(10 or 1) # 10
print('=== or for strings and empty strings')
print([] or 'hello')
print(['mine'] or 'ok')
print('' or 'hello')


#not operator for non-bools
print('====not operator for non-bools====')
print(not 'ji')  #f
print(not '')      #T
print(not True)     #F
print(not 10)       #F
print(not 0)        #T



