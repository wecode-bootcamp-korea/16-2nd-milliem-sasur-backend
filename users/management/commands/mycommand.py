import random
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from django_seed import Seed

from users.models import *
from book.models import *
from library.models import *

from faker import Faker


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--number", default=1, type=int, help="몇개 생성 하실거에요?")

    def handle(self, *args, **options):
        
        number = options.get("number")
        fake = Faker(["ko_KR"])
        seeder = Seed.seeder()
        
        
        # Book
        seeder.add_entity(
            Book,
            number,
            {
                 title            = 
                 summary          = 
                 translator       = 
                 sub_title        = 
                 description      = 
                 page             = 
                 capacity         = 
                 pub_date         = 
                 launched_date    = 
                 contents         = 
                 publisher_review = 
                 image_url        = 
                 purchase_url     = 
                 author           = 
                 sub_category     = 
                 publisher        = 
                 series           = 
                 shelf            = 
            },
        )
        # Author
        seeder.add_entity(
            Author,
            number,
            {
                "name": lambda x: fake.name(),
                "description": lambda x: fake.text(),
            },
        )
        #Publisher
        seeder.add_entity(
            Publisher,
            number,
            {
                "name": lambda x: fake.name(),
                "description": lambda x: fake.text(),
            },
        )
        
        # Subcategory
        seeder.add_entity(
            Subcategory,
            number,
            {
                "name": lambda x: fake.name(),
                "description": lambda x: fake.text(),
            },
        )
        
        #Category
        seeder.add_entity(
            Category,
            number,
            {
                "name": lambda x: fake.name(),
                "description": lambda x: fake.text(),
            },
        )
        
        # Review
        seeder.add_entity(
            Author,
            number,
            {
                "name": lambda x: fake.name(),
                "description": lambda x: fake.text(),
            },
        )
        
        # ReviewLike
        seeder.add_entity(
            Author,
            number,
            {
                "name": lambda x: fake.name(),
                "description": lambda x: fake.text(),
            },
        )
        
        seeder.add_entity(
            Author,
            number,
            {
                "name": lambda x: fake.name(),
                "description": lambda x: fake.text(),
            },
        )
        
        seeder.add_entity(
            Author,
            number,
            {
                "name": lambda x: fake.name(),
                "description": lambda x: fake.text(),
            },
        )
        
        seeder.add_entity(
            Author,
            number,
            {
                "name": lambda x: fake.name(),
                "description": lambda x: fake.text(),
            },
        )
        
        seeder.add_entity(
            Author,
            number,
            {
                "name": lambda x: fake.name(),
                "description": lambda x: fake.text(),
            },
        )

        seeder.execute()
        self.stdout.write(self.style.SUCCESS("Successfully create authors"))
