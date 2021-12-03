from django.core.checks import messages
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required 
from stream.forms import RegistrationForm, UpdateProfileForm, UpdateUserForm
from django.contrib.auth.models import User
from stream.models import Post, Profile
from django.db.models.signals import post_save
from django.dispatch import receiver

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

#post_save - signals works after a model's save() method is called.
#receiver - the function who receives the signals and does something
#sender - sends the signal
#created - checks whether the model is created or not
#instance - created model instance
#kwargs - wildcard keyword arguments
##>>>> link to the source >>>> https://medium.com/analytics-vidhya/signals-in-django-af99dabeb875  <<<<
@receiver(post_save, sender=User) #we are using receiver decorator to call the create_user_profile function on creation of user instance.
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

@login_required
@csrf_protect
def profile(request):
    if request.method == "POST":
        mtumiaji = UpdateUserForm(request.POST, instance = request.user)
        profile = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if mtumiaji.is_valid() and profile.is_valid():
            mtumiaji.save()
            profile.save()
            messages.success(request, f'The account has been updated successfully')
            return redirect('profile')

    else:
        mtumiaji = UpdateUserForm(instance=request.user)
        profile = UpdateProfileForm(instance=request.user.profile)

    user_post = Post.objects.filter(mtumiaji=request.user).order_by("-timed_created")
    post = Post.objects.filter(mtumiaji=request.user).order_by("-timed_created")

    context = {
        "user_form": mtumiaji,
        "profile_form": profile,
        "user_post": user_post,
        "posts": post,
    }
    return render(request,'registration/profile.html',context)


    