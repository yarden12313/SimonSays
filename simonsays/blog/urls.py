from django.conf.urls import url, include
from django.views.generic import ListView
from django.views.generic import DetailView
#from simonsays.blog.models import Post
from . import models

urlpatterns = [
                url(r'^$', ListView.as_view(
                                    queryset=models.Post.objects.all().order_by("-date")[:25],
                                    template_name="blog/blog.html")),
                url(r'^(?P<pk>\d+)$', DetailView.as_view(model=models.Post, template_name = 'blog/post.html'))
            ]

