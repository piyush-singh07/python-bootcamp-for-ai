#range concept

r1= range(10)
print(type(r1))
print(r1) # will give in only range(0,10)

for e in r1:
    print(e)
    
#different forms of range
#range(n)
print('=======single arg foem========')
rf1= range(5)
print(rf1)
for r in rf1:
    print(r)

#range(begin,end)
print('=======begin end form========')
rf2=range(1,6)
print(rf2)
for r in rf2:
    print(r)
    
#range(begin,end, postive step)
print('=======begin end step form========')
rf3=range(1,21,2)
print(rf3)
for r in rf3:
    print(r)
    
rf4=range(1,21,3)
print(rf4)
for r in rf4:
    print(r)
    
#range(begin,end, negative step)
print('=======begin end step form========')
rf5=range(20,1,-2)
print(rf5)
for r in rf5:
    print(r)
    
rf6=range(20,1,-5)
print(rf6)
for r in rf6:
    print(r)    

print('=========')
r9=rf6[0:3]
for e in r9:
    print(e)