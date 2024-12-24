# apple="red color" global

# def fruits():
#     return "apples are in",apple 
    
# def mango():
#     return "mangoes are  not in ",apple
    

    
# print(fruits())
# print(mango()) 
userglobal="hello"
def local():
    user="keerthan" #local variable
    print ("hello",user,userglobal)
local()
print(userglobal)
print(user) # u will get the error

# global keyword 
x=10


def add():
    global x #when we use the keyword we can modifi it
    x=x+5
    print(x)
add()

def friend():
    name="keerthan"
    age=23
    city="kamaredy"
    
    print(locals()) # by using this keyword w can print the data inside the function as the dictonary value
friend()