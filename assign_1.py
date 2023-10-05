import re
import logging

# Configur
logging.basicConfig(filename='ip_validation_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def check_ip_address(ip_str):
    # expression patterns for IPv4 and IPv6
    ipv4_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    ipv6_pattern = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'

    # the IPv4 pattern
    if re.match(ipv4_pattern, ip_str):
        return 'IPv4'
    
    # the IPv6 pattern
    if re.match(ipv6_pattern, ip_str):
        return 'IPv6'

    
    return 'Invalid'


in1 = '192.168.1.1'
in2 = '2001:0db8:85a3:0000:0000:8a2e:0370:7334'
in3 = 'NotAnIPAddress'

result1 = check_ip_address(in1)
result2 = check_ip_address(in2)
result3 = check_ip_address(in3)


logging.info(f'Result for "{in1}": {result1}')
logging.info(f'Result for "{in2}": {result2}')
logging.info(f'Result for "{in3}": {result3}')
