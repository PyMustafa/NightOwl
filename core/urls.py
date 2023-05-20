from django.urls import path
from . import views
from .views import PostListView


urlpatterns =[
    path('',PostListView.as_view(), name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logged-out/', views.loged_out, name='logged-out')
]
