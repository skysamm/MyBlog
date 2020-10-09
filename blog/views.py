from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render

from .models import Post
import datetime


class PostList(generic.ListView):
	queryset = Post.objects.filter(status=1).order_by('-created_on')
	template_name = 'index.html'

class PostDetail(generic.DetailView):
	model = Post
	template_name = 'post_detail.html'

def get_contact(request):
    return render(request, 'contact.html')