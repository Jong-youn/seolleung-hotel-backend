from django.urls        import path
from .views             import IdVerificationView, SignUpView, LoginView, UserInfoChangeView, AccountView

urlpatterns = [
    path('/id-verification', IdVerificationView.as_view()),
    path('/signup', SignUpView.as_view()),
    path('/login', LoginView.as_view()),
    path('/userinfo', UserInfoChangeView.as_view()),
    path('/account', AccountView.as_view())
]
