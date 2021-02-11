# The greeting program
from datetime import datetime

current_date = datetime.now().date()
subject = 'python'
name = 'snezhana'
print('Good day, ', name.title(),'!', current_date, 'is a perfect day to learn', subject.upper())
