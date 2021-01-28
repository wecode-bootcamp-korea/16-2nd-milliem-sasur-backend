<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
import json

from django.http      import JsonResponse
from django.views     import View
from django.db.models import Q

from book.utils       import validate_value, query_debugger
from book.models      import (
                                Book, 
                                Author, 
                                Publisher,
                                Series, 
                                Category, 
                                Review,
                                ReviewLike
                            )
# from users.utils      import login_required

class BookListView(View):
    def get(self,request):
        limit = int(request.GET.get('limit','20'))
        books = Book.objects.prefetch_related('author','subcategory').filter(subcategory_id__in = \
                                                                 [subcategory.id for subcategory in Subcategory.objects.filter(name__icontains='우리들은 자란다, 2시간으로 그 시절 나를 돌아봐요' 
                                                                    )])[0:40]
        categories = Category.objects.prefetch_related('subcatego').all()
        category_list = [{
                            'category_id': category.id,
                            'subcategory_id': subcategory.id,

        }for category in categories]
        return JsonResponse({'categories': category_list})

class SearchView(View):
    def get(self, request):
        pass
>>>>>>> 7d1eec5b17691b3ccf74b0211fbf5017380dd500
