import json

from django.test  import TestCase, Client


from my_settings    import SECRET_KEY

from library.models import Library, Shelf
from users.models   import User, UserType,Subscribe
from book.models    import (
    Book, 
    Review, 
    ReviewLike, 
    Author,
    Publisher,
    Category,
    Subcategory,
    )

class BookListTest(TestCase):
    def setUp(self):
        client = Client()
        category = Category.objects.create(id=1, name='일반소설')
        usertype = UserType.objects.create(id=1, name='모바일')
        Subscribe.objects.create(id=1, price=1)
        author = Author.objects.create(id=1, name='name', description='description', profile_image_url='profile_image_url')
        publisher = Publisher.objects.create(id=1, name='name', description='description')
        library = Library.objects.create(id=1, name='나의서재')
        shelf = Shelf.objects.create(id=1, name='나의책장', library=library)
        User.objects.create(
            id                = 1, 
            social_id         = "01058974859",
            nickname          = "nickname",
            mobile            = "01058974859",
            password          = "password",
            birth             = 900922,
            gender            = 1,
            email             = "hyeseong43@gmail.com",
            profile_image_url = "profile_image_url",
            library_image_url = "library_image_url",
            usertype          = usertype,
             )

        book = Book.objects.create(
            id               = '1',
            title            = 'title',
            summary          = 'summary',
            translator       = 'translator',
            sub_title        = 'sub_title',
            description      = 'description',
            page             = 1,
            capacity         = 1,
            pub_date         = "1990-09-22",
            launched_date    = "1990-09-22",
            contents         = 'contents',
            publisher_review = 'publisher_review',
            image_url        = 'image_url',
            purchase_url     = 'purchase_url',
            author           = author,
            category         = category,
            publisher        = publisher,
                
        )
        book.shelf.add(shelf)

    def tearDown(self):
        User.objects.all().delete()
        UserType.objects.all().delete()
        Book.objects.all().delete()
        Publisher.objects.all().delete()
        Subcategory.objects.all().delete()
        Category.objects.all().delete()
        Author.objects.all().delete()
        Library.objects.all().delete()
        Review.objects.all().delete()
        ReviewLike.objects.all().delete()
        Author.objects.all().delete()

    def test_booklist_get_success(self):
        client   = Client()
        response = client.get('/book?category_id=1')
        book     = Book.objects.get(id=1)
        self.assertEqual(response.status_code, 200)
        
        self.assertEqual(response.json(), {'bookData': {
                                              "slider"            : 
                                                                    [{
                                                                    'id'           : 1,
                                                                    'category.id'  : 1,
                                                                    'category.name': '일반소설',
                                                                    'book_id'      : 1,
                                                                    'bookTitle'    :'title',
                                                                    'bookCoverImg' :'image_url',
                                                                    'bookAuthor'   : 'name',
                                                                }],
                                              "recent_books"      : 
                                                                    [{
                                                                    'id'           : 1,
                                                                    'category.id'  : 1,
                                                                    'category.name': '일반소설',
                                                                    'book_id'      : 1,
                                                                    'bookTitle'    :'title',
                                                                    'bookCoverImg' :'image_url',
                                                                    'bookAuthor'   : 'name',
                                                                }],
                                              "favorite_books"    : 
                                                                    [{
                                                                    'id'           : 1,
                                                                    'category.id'  : 1,
                                                                    'category.name': '일반소설',
                                                                    'book_id'      : 1,
                                                                    'bookTitle'    :'title',
                                                                    'bookCoverImg' :'image_url',
                                                                    'bookAuthor'   : 'name',
                                                                }],
                                              "subcategory_list1" : 
                                                                    [{
                                                                    'id'           : 1,
                                                                    'category.id'  : 1,
                                                                    'category.name': '일반소설',
                                                                    'book_id'      : 1,
                                                                    'bookTitle'    :'title',
                                                                    'bookCoverImg' :'image_url',
                                                                    'bookAuthor'   : 'name',
                                                                }],
                                              "subcategory_list2" : 
                                                                    [{
                                                                    'id'           : 1,
                                                                    'category.id'  : 1,
                                                                    'category.name': '일반소설',
                                                                    'book_id'      : 1,
                                                                    'bookTitle'    :'title',
                                                                    'bookCoverImg' :'image_url',
                                                                    'bookAuthor'   : 'name',
                                                                }],
                                                                 }})

    def test_booklist_get_fail(self):
        client = Client()
        response = client.get('/book/cateogory_id')
        self.assertEqual(response.status_code, 404)