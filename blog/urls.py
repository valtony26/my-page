from django.urls import path
from . import views

urlpatterns = [
    path('<str:name_post>/', views.get_posts_info),
    path('<int:number_post>/', views.get_posts_number),
]