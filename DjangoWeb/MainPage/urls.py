from django.urls import path
from . import views

urlpatterns = [
    path("", views.Mainpage_index, name="mainpage_index"),
    path("<int:pk>/", views.Mainpage_detail, name="mainpage_detail"),
]
