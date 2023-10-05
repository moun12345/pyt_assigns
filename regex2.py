import regex2
import logging

logging.basicConfig(filename='email_extraction.log', level=logging.INFO, format='%(asctime)s - %(message)s')

email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}\b'

text = """
Here are some email addresses:
pooja.d@example.com
raj123@subdomain.example.co.uk
contact@company.net
"""

matches = regex2.findall(email_pattern, text)

for match in matches:
    logging.info(f'Found email address: {match}')
