#concept if we have more than one import / functions and we call it then it
#wont be any ambiguity rather most recent import of function def will be taken 

def f1():
    print('Hi I am old function')
    
def f1():
    print('Hi I am new function')
    
f1()