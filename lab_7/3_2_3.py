import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://127.0.0.1:8001')

# Print list of available methods
print(s.system.listMethods())