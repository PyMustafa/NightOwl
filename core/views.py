from django.shortcuts import render
from .models import Post
from django.views.generic import ListView
# Create your views here.


'''
def home(request):
    context ={
    "posts":Post.objects.all()
}
    return render(request, 'core/home.html', context)
'''

class PostListView(ListView):
    model = Post
    template_name = 'core/home.html'
    context_object_name = 'posts'
    


#these three methods just for testing
def register(request):
    return render(request, 'core/register.html')

def login(request):
    return render(request, 'core/login.html')

def loged_out(request):
    return render(request, 'core/logged_out.html')