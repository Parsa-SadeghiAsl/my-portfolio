from typing import Any
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.utils.html import strip_tags
from webapp.models import About, Profile, Home

from .forms import CommentForm
from .models import Post
# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog_index.html"
    paginate_by = 3
    

    def get_queryset(self):
        queryset = super().get_queryset()
        for post in queryset:
            # Modify the post content here
            post.content = strip_tags(post.content[:200]) + ' ...'  # Slice and append ellipsis
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        about = About.objects.latest('updated')
        profiles = Profile.objects.filter(about= about)
        home = Home.objects.latest('updated')
        
        context['home'] = home
        context['about'] = about
        context['profiles'] = profiles
        context["activePage"] = "blog"
        return context


def post_detail(request, slug):
    template_name = "post_detail.html"
    post = get_object_or_404(Post, slug=slug)
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about= about)
    comments = post.comments.filter(active=True).order_by("-created_on")
    home = Home.objects.latest('updated')
    activePage = "blog"
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "post": post,
            'activePage': activePage,
            'about': about,
            "profiles": profiles,
            "home": home,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )
