import socket
import logging

logging.basicConfig(filename='client_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ser_address = ('127.0.0.1', 12345)

client_socket.connect(ser_address)
logging.info(f'Connected to {ser_address}')

data_to_server = 'Hi from the client!'
client_socket.send(data_to_server.encode('utf-8'))
logging.info('Sent data to server: ' + data_to_server)

data_from_server = client_socket.recv(1024).decode('utf-8')
logging.info(f'Received data from server: {data_from_server}')

client_socket.close()