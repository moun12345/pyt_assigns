import socket
import logging

logging.basicConfig(filename='server_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

ser_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ser_address = ('127.0.0.1', 12345)

ser_socket.bind(ser_address)

ser_socket.listen(1)
logging.info('Server is listening for incoming connections...')

client_socket, client_address = ser_socket.accept()
logging.info(f'Connection established with {client_address}')

data_from_client = client_socket.recv(1024).decode('utf-8')
logging.info(f'Received data from client: {data_from_client}')

response_to_client = 'Hi from the server!'
client_socket.send(response_to_client.encode('utf-8'))
logging.info('Sent data to client: ' + response_to_client)

client_socket.close()
ser_socket.close()