import SimpleXMLRPCServer

def add(a,b):
    return a+b

def main():
    print ("Este es un servidor de procedimientos remotos")
    server = SimpleXMLRPCServer.SimpleXMLRPCServer(('0.0.0.0',8081))
    server.register_function(add)
    server.serve_forever()

if __name__ == '__main__':
    main()
