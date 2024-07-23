def keerthan():
    print("hello",1,2,5)
keerthan()

def raju(*a):
    print("HELLO",a) # by this we can pass multiple arguments 
raju(1,5,6) 

def raju1(**k):
    print("King",k) #when we use this we will get the the output as dictionary formate
raju1(a=1,c="hacked,d=5")

def outer():
    print("this is outer function")
    def inner():
        print("this is inner")
    inner()
outer()