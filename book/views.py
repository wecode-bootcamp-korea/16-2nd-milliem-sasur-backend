import random
import json

from django.http        import JsonResponse
from django.views       import View
from django.db.models   import Q, Count

from book.utils         import validate_value, query_debugger
from book.models        import Book, Review, ReviewLike

class BookListView(View):
    def get(self, request):
        try:
            category_id = int(request.GET.get('category_id',1))
            OFFSET = 0 
            LIMIT  = 10

            slider = [ {
                            'id'           :idx,
                            'category.id'  :book.category.id,
                            'category.name':book.category.name,
                            'book_id'      :book.id,
                            'bookTitle'    :book.title,
                            'bookCoverImg' :book.image_url,
                            'bookAuthor'   :book.author.name,
                        } for idx,book in enumerate(Book.objects.prefetch_related("author", "publisher")\
                        .filter(category__id=category_id).order_by('?')[OFFSET:LIMIT],1) ]

            recent_book_list = [ {
                            'id'           :idx,
                            'category.id'  :book.category.id,
                            'category.name':book.category.name,
                            'book_id'      :book.id,
                            'bookTitle'    :book.title,
                            'bookCoverImg' :book.image_url,
                            'bookAuthor'   :book.author.name,
                        } for idx,book in enumerate(Book.objects.prefetch_related('author','publisher')\
                        .filter(category__id=category_id).order_by('-pub_date')[OFFSET:LIMIT],1) ]

            favorite_books = [ {
                            'id'           :idx,
                            'category.id'  :book.category.id,
                            'category.name':book.category.name,
                            'book_id'      :book.id,
                            'bookTitle'    :book.title,
                            'bookCoverImg' :book.image_url,
                            'bookAuthor'   :book.author.name,
                        } for idx, book in enumerate(Book.objects.annotate(num_reviews=Count('reviews'))\
                        .filter(category__id=category_id).order_by('-num_reviews')[OFFSET:LIMIT],1) ]

            subcategory_list1 = [{
                            'id'           :idx,
                            'category.id'  :book.category.id,
                            'category.name':book.category.name,
                            'book_id'      :book.id,
                            'bookTitle'    :book.title,
                            'bookCoverImg' :book.image_url,
                            'bookAuthor'   :book.author.name,
                        } for idx, book in enumerate(Book.objects.prefetch_related("author", "publisher", )\
                        .filter(category__id=category_id).order_by('capacity')[OFFSET:LIMIT],1) ]

            subcategory_list2 = [{
                            'id'           :idx,
                            'category.id'  :book.category.id,
                            'category.name':book.category.name,
                            'book_id'      :book.id,
                            'bookTitle'    :book.title,
                            'bookCoverImg' :book.image_url,
                            'bookAuthor'   :book.author.name,
                        } for idx, book in enumerate(Book.objects.prefetch_related("author", "publisher", )\
                        .filter(category__id=category_id).order_by('-capacity')[OFFSET:LIMIT],1) ]
            return JsonResponse({'bookData': {
                                              "slider"            : slider,
                                              "recent_books"      : recent_book_list,
                                              "favorite_books"    : favorite_books,
                                              "subcategory_list1" : subcategory_list1,
                                              "subcategory_list2" : subcategory_list2
                                            }
                                            }, status=200)        
        except Book.DoesNotExist:
            return JsonResponse({'MESSAGE':'BOOK DOES NOT EXISTS!'},status=400)

class BookDetailView(View):
    def get(self, request, book_id):
        try :
            book = Book.objects.prefetch_related('reviews','category').get(id=book_id)
            book_detail = {
                'book_id'                : book.id,
                'title'                  : book.title,
                'image_url'              : book.image_url,
                'author'                 : book.author.name,
                'sub_title'              : book.sub_title,
                'translator'             : book.translator,
                'publisher'              : book.publisher.name,
                'description'            : book.description,
                'contents'               : book.contents,
                'publisher_descriptions' : book.publisher.description,
                'page'                   : book.page,
                'publication_date'       : book.pub_date,
                'category'               : book.category.name,
                'review_count'           : book.reviews.count(),
                }
            return JsonResponse({'book_detail':book_detail, 'like':False}, status=200)
        except Book.DoesNotExist:
            return JsonResponse({'message':'NOT_EXIST_BOOK'}, status=400)

class ReviewView(View):
    def post(self, request, book_id):
        if not Book.objects.filter(id = book_id).exists():
            return JsonResponse({"MESSAGE": "NOT_EXIST_BOOK"}, status=400)
        try :
            data = json.loads(request.body)
            user_id  = request.user
            contents = data['contents']

            if len(contents) < 200:
                review = Review.objects.create(
                    user_id  = user_id,
                    book_id  = book_id,
                    contents = contents
                )
                return JsonResponse({'message':'SUCCESS'}, status=200)
            return JsonResponse({'message':'LONG_CONTENTS'}, status=400)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
        except json.JSONDecodeError as e :
            return JsonResponse({'MESSAGE': f'Json_ERROR:{e}'}, status=400)

    def get(self, request, book_id):
        try:
            review_list = [{
                'review_id'  : review.id,
                'nick_name'  : review.user.nickname,
                'user_img'   : review.user.profile_image_url,
                'body_text'  : review.body_text,
                'pub_date'   : review.pub_date.strftime('%Y.%m.%d'),
            } for review in Book.objects.get(id=book_id).reviews.all() ]
            
            return JsonResponse({'review_list':review_list}, status=200)
        except Book.DoesNotExist:
            return JsonResponse({'message':'NOT_EXIST_BOOK'}, status=400)

    def delete(self, request, book_id):
        try :
            user_id   = request.user
            review_id = request.GET['review_id']
            review    = Review.objects.get(id=review_id)
            if review.user_id == user_id:
                review.delete()
                return JsonResponse({'message':'SUCCESS'}, status=204)
            return JsonResponse({'message':'UNAUTHORIZED'}, status=401)
        except Review.DoesNotExist:
            return JsonResponse({'message':'NOT_EXIST_REVIEW'}, status=400)

class ReviewLikeView(View):
    def patch(self, request):
        data = json.loads(request.body)
        try:
            user_id    = request.user
            review_id  = data['review_id']
            if Review.objects.filter(id=review_id).exists():
                like = ReviewLike.objects.get(user_id=user_id, review_id=review_id)
                like.delete()
                return JsonResponse({'message':'CANCEL', 'like':False}, status=200)
            return JsonResponse({'message':'NOT_EXIST_REVIEW'}, status=400)
        except ReviewLike.DoesNotExist:
            ReviewLike.objects.create(user_id=user_id, review_id=review_id)
            return JsonResponse({'message':'SUCCESS'}, status=200)

class SearchView(View) :
    def get(self, request, keyword) :
        type   = request.GET.get('type','all')
        sort   = request.GET.get('sort','keyword')
        limit  = int(request.GET.get('limit','50'))
        offset = int(request.GET.get('offset','0'))

        type_filter = {
            'all'       : Q(author__name__icontains=keyword) | Q(title__icontains = keyword) | Q(publisher__name__icontains= keyword),
            'author'    : Q(author__name__icontains=keyword),
            'title'     : Q(title__icontains = keyword) ,
            'publisher' : Q(publisher__name__icontains= keyword)
        }
        sort_dic = {
            'keyword'   : 'id',
            'page'      : '-pages',
            'published' : 'publication_date'
        }
        books = Book.objects.prefetch_related('author','category').filter(type_filter[type]).order_by(sort_dic[sort])[offset:offset+limit]
        if books :
            booklist = [ {
                "category_id"   : book.category.id,
                "category_name" : book.category.name,
                "book_id"       : book.id,
                "book_title"    : book.title,
                "book_image"    : book.image_url,
                "author"        : book.author.name                 
            } for book in books ]
            return JsonResponse({'MESSAGE': booklist }, status=200)
        return JsonResponse({'MESSAGE': 'NO_RESULT'}, status=401)
    