eno=int(input('Enter emp number: '))
ename=input('Enter emp name: ')
esal=float(input('Enter emp salary: '))
eaddr=input('Enter emp address: ')
eismarried=eval(input('Is married ? enter True for married or press enter for not married: '))
#because bool funcion works as if string is present then True is returned and if empty 
#string then False is returned
print('confirm data:')
print('Emp No. :',eno)
print('Emp Name :',ename)
print('Emp Salary :',esal)
print('Emp Address :',eaddr)
print('Emp Married :',eismarried)
