from django.urls import path
from users.views import SendSmSView, VerificationView

urlpatterns = [
    path('/sendsms', SendSmSView.as_view()),
    path('/verification', VerificationView.as_view())
]