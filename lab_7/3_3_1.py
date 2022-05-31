from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer


def lengths(*args):
    results = []
    for arg in args:
        try:
            arglen = len(arg)
        except TypeError:
            arglen = None
    results.append((arglen, arg))
    return results


def main():
    server = SimpleJSONRPCServer(('localhost', 8002))
    server.register_function(lengths)
    print("Starting server")
    server.serve_forever()

if __name__ == '__main__':
    main()
