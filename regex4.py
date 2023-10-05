import regex4
import logging

logging.basicConfig(filename='url_extraction.log', level=logging.INFO, format='%(asctime)s - %(message)s')

text = """
Here are some URLs:
https://www.example.com
Visit our website at http://example.org
Invalid URLs: ftp://ftp.example.com, www.invalid-url
"""

url_pattern = r'\bhttps?://[^\s/$.?#].[^\s]*\b'

matches = regex4.findall(url_pattern, text)

for match in matches:
    logging.info(f'Found URL: {match}')
