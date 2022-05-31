import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://localhost:8001")

multi = xmlrpc.client.MultiCall(server)
multi.getData()
multi.quadratic(1, 9, 2)

try:
    for response in multi():
        print(response)
except Exception as v:
    print("ERROR", v)
