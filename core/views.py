from django.shortcuts import get_object_or_404, render, redirect
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

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


    
class ProfilePostListView(ListView):
    model = Post
    template_name = 'core/profile.html'
    context_object_name = 'posts'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-time_posted')




    


#these three methods just for testing
def profile(request):
    return render(request, 'core/profile.html')

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'core/register.html')
    
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, f"The username '{username}' is already taken. Please try a different username.")
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, f'This email is already registered. Please use a different email.')
            return redirect('register')

        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, f'Your account has been created! You can login now')
        return redirect('login')
        

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'core/login.html')
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Logged in successfully.')
            return redirect('home') 
        
        messages.error(request, f'Invalid username or password. Please try again.')
        return redirect('login')  



# class LogoutView(View):
#     def get(self, request, *args, **kwargs):
#         logout(request)
#         return redirect('logged-out')