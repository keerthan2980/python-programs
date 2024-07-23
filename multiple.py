class father():
    def outg(self):
        print("i am  father")
        
class mother():
    def out(self):
        print("i am mother")
class child(father,mother):
    def outc(self):
        print("i am child")
h=child()
h.outg()
h.out()
h.outc()