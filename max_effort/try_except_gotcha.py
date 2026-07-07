try:
    print("A")
    raise TypeError # raise immediately exits the try block
    print("B")
except TypeError:
    print("C")
finally:
    print("D")