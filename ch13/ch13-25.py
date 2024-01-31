class A:
    def show(self):
        print('A.show called')
        
class B:
    def show(self):
        print('B.show called')
        
class C(A, B):
    pass

c = C()
c.show()