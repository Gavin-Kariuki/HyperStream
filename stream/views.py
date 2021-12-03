from django.shortcuts import render

from stream.models import Post

# Create your views here.
def home_page(request):
    post = Post.objects.all().order_by("-timed_created") #have to use timed because time is already inbuilt 

    context = {
        "posts": post,
    }

    return render(request, 'all-posts/home_page.html', context)