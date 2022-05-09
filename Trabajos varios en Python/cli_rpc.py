import xmlrpclib


def main():
    print ("Este es un cliente de procedimientos remotos")
    client = xmlrpclib.ServerProxy('http://localhost:8081')
    print client.add(10,30)

if __name__ == '__main__':
    main()
