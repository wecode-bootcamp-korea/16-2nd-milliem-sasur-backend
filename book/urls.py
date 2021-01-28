from django.urls import path
from book        import views

urlpatterns = [
    path('', views.BookListView.as_view()),
    path('', views.SearchView.as_view()),
    
]
