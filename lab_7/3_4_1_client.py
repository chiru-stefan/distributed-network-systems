import rpyc


def noisy(string):
    print ('Noisy:', repr(string))

def main():
    config = {'allow public attrs': True}
    proxy = rpyc.connect('192.168.0.145', 8003, config=config)
    fileobj = open('testfile.txt', 'r')
    linecount = proxy.root.exposed_line_counter(fileobj, noisy)
    print('The number of lines in the file was', linecount)



if __name__ == '__main__':
    main()