import json
import jwt

from django.test  import TestCase, Client

from my_settings    import SECRET_KEY, ALGORITHM
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
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'bookData': {
            "slider" : 
                [{
                'id'           : 1,
                'category.id'  : 1,
                'category.name': '일반소설',
                'book_id'      : 1,
                'bookTitle'    :'title',
                'bookCoverImg' :'image_url',
                'bookAuthor'   : 'name',
            }],
            "recent_books" : 
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

class BookDetailTest(TestCase):
    def setUp(self):
        client = Client()
        Subscribe.objects.create(id=1, price=1)
        category  = Category.objects.create(id=1, name='일반소설')
        usertype  = UserType.objects.create(id=1, name='모바일')
        author    = Author.objects.create(id=1, name='name', description='description', profile_image_url='profile_image_url')
        publisher = Publisher.objects.create(id=1, name='name', description='description')
        library   = Library.objects.create(id=1, name='나의서재')
        shelf     = Shelf.objects.create(id=1, name='나의책장', library=library)
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
            translator       = 'name',
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

    def test_bookdetail_get_success(self):
        client   = Client()
        response = client.get('/book/detail/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'book_detail': {
            'book_id'                : 1,
            'title'                  : 'title',
            'image_url'              : 'image_url',
            'author'                 : 'name',
            'sub_title'              : 'sub_title',
            'translator'             : 'name',
            'publisher'              : 'name',
            'description'            : 'description',
            'contents'               : 'contents',
            'publisher_descriptions' : 'description',
            'page'                   : 1,
            'pub_date'               : "1990-09-22",
            'category'               : '일반소설',
            'review_count'           : 0,
            }, 'like':False })

    def test_booklist_get_fail(self):
        client = Client()
        response = client.get('/book/detail=1')
        self.assertEqual(response.status_code, 404)

class BookReviewTest(TestCase):
    def setUp(self):
        client = Client()
        Subscribe.objects.create(id=1, price=1)
        category  = Category.objects.create(id=1, name='일반소설')
        usertype  = UserType.objects.create(id=1, name='모바일')
        author    = Author.objects.create(id=1, name='name', description='description', profile_image_url='profile_image_url')
        publisher = Publisher.objects.create(id=1, name='name', description='description')
        library   = Library.objects.create(id=1, name='나의서재')
        shelf     = Shelf.objects.create(id=1, name='나의책장', library=library)
        user = User.objects.create(
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
            translator       = 'name',
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
        Review.objects.create(
            user        = user,
            book        = book,
            pub_date    = '1990-09-22',
            body_text   = 'body_text',
        )

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

    def test_review_post_success(self):
        client  = Client()
        review = {'review' : "review" }
        token = 1
        response = client.post('/book/1/review', json.dumps(review), **{"HTTP_Authorization" : token}, content_type = 'application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),{'MESSAGE': 1})

    def test_review_post_fail(self):
        client  = Client()
        token = 1
        response = client.post('/book/1/review', **{"HTTP_Authorization" : token}, content_type = 'application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),{'MESSAGE': "KEY_ERROR"})

    def test_review_post_long_content(self):
        client  = Client()
        review = {
            'content' : "content"
        }
        token = 1
        response = client.post('/book/1/review', json.dumps(review), **{"HTTP_Authorization" : token}, content_type = 'application/json')

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(),{'MESSAGE': 'T00_LONG_CONTENT'})


    def test_review_get_success(self):
        client  = Client()
        token = 1
        response = client.get('/book/1/review', **{"HTTP_Authorization" : token})

        self.assertEqual(response.status_code, 200)

    def test_review_get_fail(self):
        client  = Client()
        token = 1
        response = client.get('/book/9999/review', **{"HTTP_Authorization" : token})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),{"MESSAGE": "NOT_EXIST_BOOK"})

    def test_comment_delete_success(self):
        client  = Client()
        token = 1
        response = client.delete('/book/1/review?reiview_id=1', **{"HTTP_Authorization" : token})

        self.assertEqual(response.status_code, 204)

    def test_comment_delete_fail(self):
        client  = Client()
        token = 1
        response = client.delete('/book/1/review?reiview_id=10', **{"HTTP_Authorization" : token})

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),{"MESSAGE": "NOT_EXIST_REVIEW"})

    def test_comment_delete_except(self):
        client  = Client()
        token = 1
        response = client.delete('/book/1/review?reiview_id=1', **{"HTTP_Authorization" : token})

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(),{"MESSAGE": "NOT_THIS_USER"})

class ReviewLikeTest(TestCase):
    
    def setUp(self):
        client = Client()
        Subscribe.objects.create(id=1, price=1)
        category  = Category.objects.create(id=1, name='일반소설')
        usertype  = UserType.objects.create(id=1, name='모바일')
        author    = Author.objects.create(id=1, name='name', description='description', profile_image_url='profile_image_url')
        publisher = Publisher.objects.create(id=1, name='name', description='description')
        library   = Library.objects.create(id=1, name='나의서재')
        shelf     = Shelf.objects.create(id=1, name='나의책장', library=library)
        user = User.objects.create(
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
            translator       = 'name',
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
        Review.objects.create(
            user        = user,
            book        = book,
            pub_date    = '1990-09-22',
            body_text   = 'body_text',
        )

    def tearDown(self):
        User.objects.all().delete()
        UserType.objects.all().delete()
        Book.objects.all().delete()
        Publisher.objects.all().delete()
        Subcategory.objects.all().delete()
        Category.objects.all().delete()
        Review.objects.all().delete()
        ReviewLike.objects.all().delete()

    def test_reviewlike_patch_success(self):
        client  = Client()
        review = {
            'reiview_id' : 2
        }
        token = 1
        response = client.patch('/book/reviewlike', json.dumps(review), **{"HTTP_Authorization" : token}, content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"MESSAGE": "SUCCESS", "likebutton" : True })

    def test_reviewlike_patch_cancel(self):
        client  = Client()
        review = {
            'reiview_id' : 1
        }
        token = 1
        response = client.patch('/book/reviewlike', json.dumps(review), **{"HTTP_Authorization" : token}, content_type = 'application/json')
        self.assertEqual(response.status_code, 204)

    def test_reviewlike_patch_fail(self):
        client  = Client()
        review = {
            'reiview_id' : 5
        }
        token = 1
        response = client.patch('/book/reviewlike', json.dumps(review), **{"HTTP_Authorization" : token}, content_type = 'application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"MESSAGE": "NOT_EXIST_REVIEW"})