c="hello123"
a=0
ma=3

while a<=ma:
    s=input("enter the password:")
    
    if s==c:
        print(f"correct u r password is {c}")
    else:
        print(f"incorrect {s}")
        a +=1 
    if a==ma:
        print("soorry")
    