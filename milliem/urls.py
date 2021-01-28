from django.urls import path, include


urlpatterns = [
    # path('user', include('users.urls')),
    # path('library', include('library.urls')),
    path('book', include('book.urls')),
]
