from django.core.checks import messages
from django.shortcuts import redirect, render
from stream.forms import RegistrationForm
from django.contrib.auth.models import User
from stream.models import Post, Profile

# Create your views here.
def home_page(request):
    post = Post.objects.all().order_by("-timed_created") #have to use timed because time is already inbuilt 

    context = {
        "posts": post,
    }

    return render(request, 'all-posts/home_page.html', context)


def register(request):
    if request.method == "POST":
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            registerForm.save()

            for user in User.objects.all():
                Profile.objects.get_or_create(mtumiaji = user) #get_or_create returns the object that it got and a boolean value that specifies whether the object was created or not.
                # basically get_or_create is for avoiding duplicates

                username = registerForm.cleaned_data.get('username') #cleaned_data returns a dic of validated form input fields and their values
                messages.success(request, f'An account has been created for {username}')
                return redirect('login')

    else:
        registerForm = RegistrationForm()

    return render(request, 'registration/register.html', {"form":registerForm})