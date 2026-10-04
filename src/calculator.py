def fun1(x, y):
    """Adds x and y."""
    return x + y

def fun2(x, y):
    """Subtracts y from x."""
    return x - y

def fun3(x, y):
    """Multiplies x and y."""
    return x * y

def fun4(x, y):
    """Returns the sum of fun1, fun2 and fun3."""
    return fun1(x, y) + fun2(x, y) + fun3(x, y)
