from django.urls import path
from . import views
from .views import PostListView, RegisterView, LoginView, ProfilePostListView
from django.contrib.auth import views as auth_views


urlpatterns =[
    path('',PostListView.as_view(), name='home'),
    path('profile/<str:username>',ProfilePostListView.as_view(), name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    # path('loggedout/', LogoutView.as_view(), name='logged-out')
    path('logged-out/',auth_views.LogoutView.as_view(template_name='core/logged_out.html'), name='logged-out' ),
]
