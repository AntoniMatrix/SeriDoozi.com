import sys
import os

# تنظیم encoding
sys.stdout.reconfigure(encoding='utf-8') if hasattr(sys.stdout, 'reconfigure') else None
sys.stderr.reconfigure(encoding='utf-8') if hasattr(sys.stderr, 'reconfigure') else None

# تنظیم متغیر محیطی
os.environ['PYTHONIOENCODING'] = 'utf-8'
os.environ['LANG'] = 'en_US.UTF-8'

# اضافه کردن مسیر پروژه
sys.path.insert(0, os.path.dirname(__file__))

from workshop_tailoring.wsgi import application
