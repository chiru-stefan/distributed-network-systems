import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://192.168.0.145:8001')
print(s.addtogether(1,2,3))

# Print list of available methods
# print(s.system.listMethods())