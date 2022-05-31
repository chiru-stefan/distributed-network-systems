from jsonrpclib import Server

def main():
    proxy = Server('http://localhost:8002')
    print(proxy.lengths((1, 2, 3), 27, {'Sirius': 123, 'Tarantula': 324}))


if __name__ == '__main__':
    main()