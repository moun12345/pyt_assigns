import regex3
import logging

logging.basicConfig(filename='date_extraction.log', level=logging.INFO, format='%(asctime)s - %(message)s')

text = """
Here are some dates:
04/09/2023
22/40/2022
09/19/20
Invalid dates: 35/13/2022, 02/29/2021
"""
date_pattern = r'\b\d{2}/\d{2}/\d{4}\b'

matches = regex3.findall(date_pattern, text)

for match in matches:
    logging.info(f'Found date: {match}')
