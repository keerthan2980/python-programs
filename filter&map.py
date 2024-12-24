numbers=[1,2,3,4,5,6,7,8,9,10]

def hello(even):
    return even%2==0
    
# result = filter(hello,numbers)
# print(list(result))
# print(set(result))  #empty u will get
 # we can get the result only once when we use filter if u want u can change the result varaible 

result = filter(hello,numbers)
result2 = filter(hello,numbers)
print(list(result))
print(set(result2))