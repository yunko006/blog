from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost
from .forms import PostForm  # , EntryForm

# Create your views here.


def home(request):
    """Show all blogs at the index"""
    blogs = BlogPost.objects.order_by("-date_added")
    context = {"blogs": blogs}
    return render(request, "blogs/home.html", context)


def post(request, post_id):
    """Show a single post and all its text"""
    post = BlogPost.objects.get(id=post_id)
    entries = post.text
    context = {"post": post, "entries": entries}
    return render(request, "blogs/post.html", context)


@login_required
def new_post(request):
    """Add a new post"""
    if request.method != "POST":
        # No data submitted, create a blank form
        form = PostForm()

    else:
        # Post data submitted; process data
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect("blogs:home")

    # Display a blank or invalid form
    context = {"form": form}
    return render(request, "blogs/new_post.html", context)


@login_required
def edit_entry(request, post_id):
    """Edit an existing entry """
    post = BlogPost.objects.get(id=post_id)
    text = post.text
    check_topic_owner(request, post)

    if request.method != "POST":
        # Initial request; pre=fill form with the current entry
        form = PostForm(instance=post)
    else:
        # POST data submitted; process data.
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogs:home") #, post_id=post.id)

    context = {"post": post, "text": text, "form": form}
    return render(request, "blogs/edit_entry.html", context)


# def delete_entry(request, post_id):
#     """Delete an existing entry"""
#     post = BlogPost.objects.get(id=post_id)
#     entry = post.text

#     if request.method == 'POST':
#         entry.delete()
#         return redirect('blogs:home')

#     context = {'post': post, 'entry': entry}
#     return render(request, 'blogs/delete_entry.html', context)


@login_required
def delete_post(request, post_id):
    """Delete an existing post"""
    post = BlogPost.objects.get(id=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('blogs:home')

    context = {"post": post}
    return render(request, 'blogs/delete_post.html', context)

def check_topic_owner(request, post):
    if post.owner != request.user:
        raise Http404