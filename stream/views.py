from django.shortcuts import render

from stream.models import Post

# Create your views here.
def home_page(request):
    post = Post.objects.all().order_by("-created")

    context = {
        "posts": post,
    }

    return render(request, 'home_page.html', context)