from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import NewUserForm
from posts.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Views
@login_required
def home(request):
    post = Post.objects.order_by('-created')
    page = request.GET.get('page', 1)

    paginator = Paginator(post, 2)
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    return render(request, "registration/home.html", {'post': post})


def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewUserForm()
    return render(request, 'registration/register.html', {'form': form})


def error_404(request, exception):
    return render(request, 'registration/404.html', status=404)


def server_error(request, exception=None):
    return render(request, 'registration/500.html')
