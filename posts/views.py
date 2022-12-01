from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostsForm
from .models import Post


def create_post(request):
    error = ''
    if request.method == 'POST':
        form = PostsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form is not valid.'

    form = PostsForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'posts/create_post.html', data)


def wishlist(request):
    return render(request, 'posts/wishlist.html')


def add_to_wishlist(request, id):
    post = get_object_or_404(Post, id=id)
    if post.user_wishlist.filter(id=request.user.id).exists():
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        post.user_wishlist.add(request.user)
    return render(request, 'posts/wishlist.html', {'post': post})


def delete_from_wishlist(request, id):
    post = get_object_or_404(Post, id=id)
    if post.user_wishlist.filter(id=request.user.id).exists():
        post.user_wishlist.remove(request.user)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        return render(request, 'registration/profile.html', {'post': post})



