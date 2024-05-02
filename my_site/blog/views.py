from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Post
from .forms import CommentForm

from django.views.generic import ListView
from django.views import View

# Create your views here.


def get_date(post):
  return post.get('date') #or we can type posts['date']

class StartingPageView(ListView):
  template_name = 'blog/starting.html'
  model = Post
  ordering = ['-Date']
  context_object_name = 'posts'

  def get_queryset(self):
    queryset = super().get_queryset()
    data = queryset[:3]
    return data

'''
def starting_page(request):
  latest_posts = Post.objects.all().order_by("-Date")[:3] #this query take the rassing 3 posts
  return render(request, 'blog/starting.html', {
    'posts': latest_posts
  })
'''


class AllPostsView(ListView):
  template_name = 'blog/all-posts.html'
  model = Post
  ordering = ["-Date"]
  context_object_name = 'all_posts'

'''
def posts(request):
  all_posts = Post.objects.all().order_by('Date')
  return render(request, 'blog/all-posts.html', {
    'all_posts': all_posts,
  })
'''


class SinglePostView(View):

  def is_stored_post(self, request, post_id):
    stored_posts = request.session.get('stored_posts')
    if stored_posts is not None :
      is_saved_for_later = post_id in stored_posts
    else:
      is_saved_for_later = False

    return is_saved_for_later



  def get(self, request, slug):
    post = Post.objects.get(Slug= slug)
   
    context = {
      'post': post,
      'post_tags': post.tags.all(),
      'comment_form': CommentForm(),
      'comments' : post.comments.all().order_by('-id'),
      'saved_for_later': self.is_stored_post(request, post.id)
    }
    return render(request, 'blog/post-detail.html', context)
 
  def post(self, request, slug):
    comment_form = CommentForm(request.POST)
    post = Post.objects.get(Slug= slug)

    if comment_form.is_valid():
      comment = comment_form.save(commit=False)
      comment.post = post
      comment.save()
      return HttpResponseRedirect(reverse('post-detail-page', args=[slug]))

    context = {
      'post': post,
      'post_tags': post.tags.all(),
      'comment_form': comment_form,
      'comments' : post.comments.all().order_by('-id'),
      'saved_for_later': self.is_stored_post(request, post.id)
    }
    return render(request, 'blog/post-detail.html', context)
  
'''
def post_detail(request, slug):
  identified_post = get_object_or_404(Post, Slug = slug)
  return render(request, 'blog/post-detail.html', {
    'post': identified_post,
    'post_tags': identified_post.tags.all()
  })
'''



class ReadLaterView(View):


  def get(self, request):
    stored_post = request.session.get('stored_posts')

    context = {}

    if stored_post is None or len(stored_post) == 0:
      context['posts'] = []
      context['has_posts'] = False
    else:
      posts = Post.objects.filter(id__in=stored_post)
      context['posts'] = posts
      context['has_posts'] = True

    return render(request, 'blog/stored-posts.html', context)

  def post(self, request):
    stored_post = request.session.get('stored_posts')

    if stored_post is None:
      stored_post = []
    
    post_id = int(request.POST['post_id'])

    if post_id not in stored_post:
      stored_post.append(post_id) #add post_id to the session
    else:
      stored_post.remove(post_id) #remove post_id to the session

    request.session['stored_post'] = stored_post

    return HttpResponseRedirect('/')

    