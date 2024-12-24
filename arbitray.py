#arbitray arguments 
# when we dont know number of arguments is passed

def ars(*unknow): #ars(*args)
    print(unknow)
    print(type(unknow))
    
ars("hello",123,{"kee":"yello"})

