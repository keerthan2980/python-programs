class parent():
    def out(self):
        print("i am parent")
class child(parent):
    def outc(self):
        print("i am child")
h=child()
h.outc()
h.out()