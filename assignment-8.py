"""
1) Create 2 classes for single inheritance named respectively A(base class) and B(derived class)

2) Create 3 data members in class A: a(private), b(protected) and c(public) initialise their values in a parameterized constructor

3) Create a method known as display in both the classes, to display the values of a,b and c

4) While accessing the private member an exception should be raised and a personalized message should be displayed and the exception should be handled properly so that the rest of the code can get executed
"""


class A:
    def __init__(self, a, b, c):
        self.__a = a
        self._b = b
        self.c = c

    def display(self):
        print(f"a: {self.__a} b: {self._b} c: {self.c}")


class B(A):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def display(self):
        super().display()


try:
    a = A(10, 20, 30)
    print("values in A: ")
    a.display()

    b = B(100, 200, 300)
    print("values in B: ")
    b.display()

    print(a.__a)
except AttributeError:
    print("Cannot access the private member (__a) in class A or class B")
