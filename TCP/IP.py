import socket

host = '127.0.0.1'
post = 8081

def request(client):
    b = client.recv(1024)
    client.send('HTTP/1.1 200 ok\r\n\r\n'.encode('utf-8'))
    with open('index.html','rb') as f:
        data = f.read()
    client.send(data)

def main():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, post))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        request(conn)
        conn.close()
if __name__ == '__main__':

    main() 