from django.urls import path
from users.views import (
#    SendSmSView, 
    VerificationView, 
    MobileSignUp, 
    MobileSignIn, 
    KakaoView
)

urlpatterns = [
#    path('/sendsms', SendSmSView.as_view()),
    path('/verification', VerificationView.as_view()),
    path('/mobile_signup', MobileSignUp.as_view()),
    path('/mobile_signin', MobileSignIn.as_view()),
    path('/kakao', KakaoView.as_view())
]
