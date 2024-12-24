import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project1.settings')
# print("t his is problem")
# print("this is working or  my system ")

application = get_wsgi_application()
