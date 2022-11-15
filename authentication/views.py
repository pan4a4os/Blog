from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewUserForm
from posts.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Views
@login_required
def home(request):
    post = Post.objects.order_by('-created')
    page = request.GET.get('page', 1)

    paginator = Paginator(post, 1)
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    return render(request, "registration/home.html", {'post': post,})


def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewUserForm()
    return render(request, 'registration/register.html', {'form': form})


