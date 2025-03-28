class A:
    def __init__(self):
        print("Init in A")

    def feature1(self):
        print("Feature1")

		
class B():
    def __init__(self):
        print("Init in B")
            
    def feature2(self):
        print("Feature2")

class C(A, B):
    def __init__(self):
        print("Init in C")
        super().__init__()


b = B()
c = C()
c.feature1()
c.feature2()