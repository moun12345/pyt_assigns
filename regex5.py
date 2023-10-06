import regex5
import logging

logging.basicConfig(filename='password_validation.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def vali_pwd(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
    
    if regex5.match(pattern, password):
        return True
    else:
        return False

# Test cases
passwords = [
    "P@ssw0rd",  
    "Abcdefg1",  
    "rose",  
    "mon",      
]

for password in passwords:
    if vali_pwd(password):
        logging.info(f'Valid password: {password}')
    else:
        logging.info(f'Invalid password: {password}')
