import rpyc


def main():
    print("Starting server")
    from rpyc.utils.server import ThreadedServer

    t = ThreadedServer(MyService, port=8003)
    t.start()


class MyService(rpyc.Service):
    def exposed_line_counter(self, fileobj, function):
        print('file obj:', fileobj)
        print('function:', function)
        print('Client has invoked exposed_line_counter()')

        for linenum, line in enumerate(list(fileobj)):
            function(line.replace('\n', ''))
        return linenum + 1


if __name__ == '__main__':
    main()