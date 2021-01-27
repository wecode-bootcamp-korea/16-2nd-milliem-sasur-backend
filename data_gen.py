import os
import django
import random

from faker          import Faker
from book.models    import *
from library.models import *
from users.models   import *

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'milliem.settings')
# django.setup()

fake = Faker()

def add_user(N=20):
    for i in range(N):
        # User.objects.create(
        #     nickname=fake.name()
        #     mobile=fake.mobile()
        #     password=fake.password()
        #     birth=fake.
        # )
        print(fake.name)
        pass

add_user()
