from datetime import datetime
from pytz import timezone
import time

def timestamp_to_date(timestamp):
    timestamp = float(timestamp)
    dt = datetime.fromtimestamp(timestamp, tz=timezone("GMT"))
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def convert_date_to_timestamp(date_string, date_format="%Y-%m-%d %H:%M:%S"):
    """
    Convert a date string to a timestamp.
    
    Args:
    date_string (str): The date string to convert.
    date_format (str): The format of the date string. Default is "%Y-%m-%d %H:%M:%S".
    
    Returns:
    int: The timestamp equivalent of the date.
    """
    try:
        # Convert the date string to a datetime object
        dt_obj = datetime.strptime(date_string, date_format)
        
        # Convert the datetime object to timestamp
        timestamp = int(time.mktime(dt_obj.timetuple()))
        return timestamp
    except ValueError as e:
        return f"Error: {e}"