from django.urls import path
from book        import views

urlpatterns = [
    path('', views.BookListView.as_view()),
    path('/detail/<int:book_id>', views.BookDetailView.as_view()),
    path('/<int:book_id>/review', views.ReviewView.as_view()),
    path('/reviewlike', views.ReviewLikeView.as_view()),
    path('/search/<str:keyword>', views.SearchView.as_view()),
]