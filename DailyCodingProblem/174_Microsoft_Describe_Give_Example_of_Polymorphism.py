"""
This problem was asked by Microsoft.

Describe and give an example of each of the following types of polymorphism:

    - Ad-hoc polymorphism
    - Parametric polymorphism
    - Subtype polymorphism
"""

# Polymorphism is the ability of an object to take on many forms

# Ad-hoc polymorphism:
#   ad-hod means created or done for a particular purpose as necessary
#   Therefore, ad-hoc polymorphism is a type of polymorphism where you can implement
#   and overload functions based on different types
#
#   Example:

#   NOTE: python does not support function overloading because its dynamically typed
#   using the multipledsipatch library can solve this, but this form of polymorphism is
#   not inherently supported by python
#   further reading: https://www.artima.com/weblogs/viewpost.jsp?thread=101605
from multipledispatch import dispatch

@dispatch(int, int)
def add_func(a, b):
    return a+b

@dispatch(int, int, int)
def add_func(a, b, c):
    return a+b+c

print(add_func(1,2))
print(add_func(1, 2, 3))

#   another example of ad-hoc polymorphism in python is the + operator
#   it behaves differently when its given a number vs. when its given strings
#   or lists. This is because its been overloaded:
#   For example:
#       - For numbers, we need to do addition
#             - For ints, the + operator does integer addition
print(3+3)
#             - For floats, the + operator does floating point addition
print(1.2 + 2.1)
#       - For strings its does string concatenation
print("add-hoc " + "polymorphism")
#       - For lists it does list concatenation
print([1, 2, 3] + [4, 5, 6])


# Parametric polymorphism:
#   This deals with creating generic implementations that are data-type independent
#   For example the append function of python list is data-type independent
#   it works the same way when you provide ints or strings:

l = [1, 2, 3]
l.append(4)
print(l)
l.append('five')
print(l)

# Subtype Polymorphism
#   This type of polymorphism is specific to interfaces. We be subclass a
#   super-class we use define all the super-class's methods to implement a
#   specific interface (or use the default interface). This allows us to
#   create implementations of the super-class that remain consistent regards to
#   its interface.
#
#   For example:

class Shape:
    def draw(self):
        print("Drawing a shape")


class Circle(Shape):
    def draw(self):
        print("Drawing Circle")


class Sqaure(Shape):
    def draw(self):
        print("Drawing Square")

shape = Shape()
circle = Circle()
square = Sqaure()
for shape in [square, circle, shape]:
    shape.draw()


# Further reading on subtype vs. inheritance
# https://stackoverflow.com/questions/23592131/what-is-the-difference-between-subtyping-and-inheritance-in-oo-programming#:~:text=In%20the%20object%2Doriented%20framework,refers%20to%20compatibility%20of%20interfaces.&text=Inheritance%20refers%20to%20reuse%20of%20implementations.
