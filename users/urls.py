from django.urls        import path
from .views             import IdVerificationView, SignUpView, LoginView, UserInfoChangeView, AccountFindView, PasswordFindView

urlpatterns = [
    path('/id-verification', IdVerificationView.as_view()),
    path('/signup', SignUpView.as_view()),
    path('/login', LoginView.as_view()),
    path('/mypage/userinfo', UserInfoChangeView.as_view()),
    path('/account-find', AccountFindView.as_view()),
    path('/password-find', PasswordFindView.as_view())   
]
