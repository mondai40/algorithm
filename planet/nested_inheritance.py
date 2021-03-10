class A:
    def call_me(self):
        print("I am A")

class B:
    def call_me(self):
        print("I am B")
        
class C(A, B):
    def call_me(self):
        print("I am C")
        A.call_me(self)
        B.call_me(self)
        
class D(C):
    def call_me(self):
        print("I am D")
        C.call_me(self)
        
d = D()
d.call_me()
