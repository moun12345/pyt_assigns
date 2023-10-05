import regex1
import logging

logging.basicConfig(filename='ph_no_extraction.log', level=logging.INFO, format='%(asctime)s - %(message)s')

text = """
Here are some phone numbers:
(123) 456-7891
123-456-7891
123 456 7891
1234567891
12-345-67891
555-123
Invalid numbers: 12345, 123-45-67891, (123)4567891
"""

ph_no_pattern = r'\(?\d{3}\)?[- ]?\d{3}[- ]?\d{4}'

matches = regex1.findall(ph_no_pattern, text)

for match in matches:
    logging.info(f'Found phone number: {match}')
