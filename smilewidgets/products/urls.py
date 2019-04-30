from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path(r'^$',views.enquiryList.as_view()),
    path(r'<int:productcode>/<str:date>/', views.enquiryDetail.as_view()),
    path(r'<int:productcode>/<str:date>/<str:giftCardCode>/', views.enquiryDetail.as_view()),
]

