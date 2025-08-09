#Byte and ByteArray concept
#bytes always are in the range 0 to 256

list1=[1,2,3,4,5]
b= bytes(list1)
print(type(b))
print(b)
print('===print values===')

for v in b:
    print(v)
    
list2=[10,90,89,900,991]
print(list2)
#bt=bytes(list2) #will give error bytes range is 0 to 255
 
