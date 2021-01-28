import random
import datetime

from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from django_seed import Seed

# from users.models import *
# from book.models import *
# from library.models import *

from faker import Faker

# print(__name__)
from data import seed_info


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--number", default=30, type=int, help="몇개 생성 하실거에요?")

    def handle(self, *args, **options):
        print(seed_info.__name__)


#         number = options.get("number")
#         fake   = Faker(["ko_KR"])
#         seeder = Seed.seeder()

#         start_date            = datetime.date(1980, 1, 1)
#         end_date              = datetime.date(2020, 1, 1)
#         time_between_dates    = end_date - start_date
#         days_between_dates    = time_between_dates.days
#         random_number_of_days = random.randrange(days_between_dates)
#         random_date = start_date + datetime.timedelta(days=random_number_of_days)

#         seeder.add_entity(
#             Book,
#             number,
#             {
#                  title            = lambda x: random.choices(seed_info.book_summary,
#                  summary          = lambda x: random.choices(seed_info.book_summary),
#                  translator       = lambda x: fake.name(),
#                  sub_title        = lambda x: fake.sentence(),
#                  description      = lambda x: fake.text(),
#                  page             = lambda x: random.randint(300, 1000)
#                  capacity         = lambda x: f'{random.randint(25, 1000)}MB'
#                  pub_date         = lambda x: fake.date(),
#                  launched_date    = lambda x: fake.date(),
#                  contents         = lambda x: fake.text(),
#                  publisher_review = lambda x: fake.text(),
#                  image_url        = lambda x: fake.name(),
#                  purchase_url     = lambda x: fake.name(),
#                  author           = lambda x: Author.objects.
#                  sub_category     = lambda x: fake.name(),
#                  publisher        = lambda x: fake.name(),
#                  series           = lambda x: fake.name(),
#                  shelf            = lambda x: fake.name(),
#         #     },
#         # )
#         # # Author
#         # seeder.add_entity(
#         #     Author,
#         #     number,
#         #     {
#         #         "name": lambda x: fake.name(),
#         #         "description": lambda x: fake.text(),
#         #     },
#         # )
#         # Publisher 30개 작성 완료 !
#         # seeder.add_entity(
#         #     Publisher,
#         #     number,
#         #     {
#         #         "name": lambda x: fake.name(),
#         #         "description": lambda x: fake.text(),
#         #     },
#         # )

#         # # Subcategory ! 이미 40개 작성 완료
#         # seeder.add_entity(
#         #     Subcategory,
#         #     number,
#         #     {
#         #         "name": lambda x: fake.name(),
#         #         "description": lambda x: fake.text(),
#         #     },
#         # )

#         # #Category # 이미 디비 4개 있음!
#         # seeder.add_entity(
#         #     Category,
#         #     number,
#         #     {
#         #         "name": lambda x: fake.name(),
#         #         "description": lambda x: fake.text(),
#         #     },
#         # )

#         # # Review # 관계 작성 필요
#         # seeder.add_entity(
#         #     Author,
#         #     number,
#         #     {
#         #         "name": lambda x: fake.name(),
#         #         "description": lambda x: fake.text(),
#         #     },
#         # )

#         # # ReviewLike
#         # seeder.add_entity(
#         #     Author,
#         #     number,
#         #     {
#         #         "name": lambda x: fake.name(),
#         #         "description": lambda x: fake.text(),
#         #     },
#         # )

#         # seeder.add_entity(
#         #     Author,
#         #     number,
#         #     {
#         #         "name": lambda x: fake.name(),
#         #         "description": lambda x: fake.text(),
#         #     },
#         # )

#         # seeder.add_entity(
#         #     Author,
#         #     number,
#         #     {
#         #         "name": lambda x: fake.name(),
#         #         "description": lambda x: fake.text(),
#         #     },
#         # )

#         # seeder.add_entity(
#         #     Author,
#         #     number,
#         #     {
#         #         "name": lambda x: fake.name(),
#         #         "description": lambda x: fake.text(),
#         #     },
#         # )

#         # User
#         seeder.add_entity(
#             Author,
#             number,
#             {
#                 # social_id         =
#                 nickname          : lambda x: fake.name(),
#                 mobile            = lambda x: fake.phone_number()
#                 password          = '1111'
#                 birth             = lambda x: fake.date_of_birth()
#                 gender            = lambda x: random.choice(["남", "여"])
#                 email             = fake.ascii_free_email()
#                 profile_image_url =
#                 library_image_url =
#                 usertype          =
#                 subscribe         =
#                 review            =
#                 library           =

#             },
#         )

#         seeder.execute()
#         self.stdout.write(
#             self.style.SUCCESS("Successfully Finished to Create Model's Data")
#         )
