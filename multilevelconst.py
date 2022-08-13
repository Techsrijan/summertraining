class A:
    def __init__(self):
        print("this is class A")

class B(A):
    '''
    def __init__(self):
        print("this is class B")
'''
class C(B):
    '''def __init__(self):
        print("this is class C")
  '''
cc=C()