from django.urls        import path
from .views             import (
    InquiryView,
    InquiryUpdateView,
    InquiryTypeView
    )

urlpatterns = [
    path('', InquiryView.as_view()),
    path('/<int:inquiry_id>', InquiryUpdateView.as_view()),
    path('/type', InquiryTypeView.as_view()),
]
