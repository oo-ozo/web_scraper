import socket
import requests

class raw_sock():

    def __init__(self, name):
        self.name = name

    def req(self):
        s = socket.socket()
        s.connect((self.name, 80))
        self.text = 'GET / HTTP/1.1\r\nHost: {}\r\n\r\n'.format(self.name)    
        s.send(self.text.encode())
            
        data = s.recv(1024)
        return data.decode('utf-8')
            

    def ip(self):
        return socket.gethostbyname(self.name)

class inter_file():
    def __init__(self, url):
        self.url=url

    def find(self):
        self.re = requests.get(self.url+"/robots.txt")
        return self.re
        
    def show(self):
        self.re = requests.get(self.url+"/robots.txt")
        return self.re.text
        
    def write_file(self, file):
        self.ul = requests.get(self.url)
        self.file = file
        with open(self.file, 'w') as file:
            file.write(ul.text)
        


