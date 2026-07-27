# in multiclass inheritence super() calls the function in class left to right.
class A:
    def f(self):
        return "A"

class B(A):
    def f(self):
        return "B" + super().f()

class C(A):
    def f(self):
        return "C" + super().f()

# first B, then C then A 
class D(B, C):
    pass

print(D().f())