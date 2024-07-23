class grandfather():
    def outg(self):
        print("i am grand father")
class parent(grandfather):
    def out(self):
        print("i am parent")
class child(parent):
    def outc(self):
        print("i am child")
h=child()
h.outg()
h.outc()
h.out()