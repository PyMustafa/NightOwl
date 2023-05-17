from django.shortcuts import render
from .models import Post
from django.views.generic import ListView
# Create your views here.



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
    paginate_by = 5
'''