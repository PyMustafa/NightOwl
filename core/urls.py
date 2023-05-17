from django.urls import path
from . import views


urlpatterns =[
    path('',views.home, name='home')
    #path('',PostListView.as_view(), name='home')
]