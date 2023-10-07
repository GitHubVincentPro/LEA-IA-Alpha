# Dans app/utils.py

from datetime import datetime

def format_date(date):
return datetime.strftime(date, "%d/%m/%Y")