import operator, math
from xmlrpc.server import SimpleXMLRPCServer
from functools import reduce

def main():
    server = SimpleXMLRPCServer(('0.0.0.0', 8001))
    server.register_function(addtogether)
    server.register_function(quadratic)
    server.register_function(remote_repr)
    server.register_function(getData)
    server.register_introspection_functions()
    server.register_multicall_functions()

    print ("Server ready")
    server.serve_forever()

def addtogether (*things) :
    """Add together everything in the list “things*."""
    return reduce(operator.add, things)

def quadratic(a, b, c):
    """Determine “x values satisfying: “a* * x*x + “b* * x +c == o"""
    b24ac = math.sqrt(b*b - 4.0*a*c)
    return list(set([ (-b-b24ac) / 2.0*a,  (-b+b24ac) / 2.0*a ]))

def remote_repr (arg):
    """Return the “repr()* rendering of the supplied “arg*."""
    return arg

def getData():
    return "Hello World! This is C.S"

if __name__ == '__main__':
    main()
