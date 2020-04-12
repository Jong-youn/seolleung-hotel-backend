from django.urls        import path
from .views             import (
    IdVerificationView, 
    SignUpView, 
    LoginView, 
    UserInfoChangeView, 
    AccountFindView, 
    PasswordFindView, 
    SmsAuthenticationView,
    UserPasswordChangeView, 
    JobView,
    KakaoLoginView
    )


urlpatterns = [
    path('/id-verification', IdVerificationView.as_view()),
    path('/signup', SignUpView.as_view()),
    path('/login', LoginView.as_view()),
    path('/userinfo', UserInfoChangeView.as_view()),
    path('/account-find', AccountFindView.as_view()),
    path('/password-find', PasswordFindView.as_view()),
    path('/sms-auth', SmsAuthenticationView.as_view()),
    path('/userpw', UserPasswordChangeView.as_view()),
    path('/job', JobView.as_view()),
    path('/kakao', KakaoLoginView.as_view())
]
