from django.shortcuts import render, redirect,get_object_or_404
from .forms import PostForm
from .models import Post


def product_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'product/product_list.html', context)

def product_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'product/product_detail.html', {'post': post})

def product_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('product_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'product/product_create.html', {'form': form})

def product_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('product_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'product/product_create.html', {'form': form})

def product_delete(request,pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('/')


