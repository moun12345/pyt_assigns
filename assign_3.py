import datetime
import logging
import pytz

# Configure 
logging.basicConfig(filename='timezone_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

timezones = ['America/New_York', 'Europe/London', 'Asia/Tokyo']

for timezone in timezones:
    try:
        tz = pytz.timezone(timezone)
        cur_time = datetime.datetime.now(tz)
        frmt_time = cur_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')
        logging.info(f'Current time in {timezone}: {frmt_time}')
    except pytz.exceptions.UnknownTimeZoneError:
        logging.error(f'Invalid timezone: {timezone}')
