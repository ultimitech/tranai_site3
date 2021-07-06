from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Translation

def all_translations(request):
  pass

def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
  name = 'John'
  month = month.capitalize()
  # conver month from naem to number
  month_number = list(calendar.month_name).index(month)
  month_number = int(month_number)
  # 
  cal = HTMLCalendar().formatmonth(year, month_number)
  # get current year
  now = datetime.now()
  current_year = now.year

  return render(request, 'tranai/home.html', {
    'name': name,
    'year': year,
    'month': month,
    'month_number': month_number,
    'cal': cal,
    'current_year': current_year,
  })