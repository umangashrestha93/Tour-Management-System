from django.urls import path
from . import views
from .  views import ad_homeView, enroll, pack_detailView, homeView, homepage

urlpatterns = [
    path('ad-home/', ad_homeView.as_view(), name="ad_homeView"),
    path('', homeView.as_view(), name="homeView"),
    path('details/<int:pk>', pack_detailView.as_view(), name="pack_detailView"),
    path('enroll/<int:pk>', enroll.as_view(), name="enrollView"),
    path('home/',views.homepage, name="homepage"),
]
