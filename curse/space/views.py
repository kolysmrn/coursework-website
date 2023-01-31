from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework import viewsets
from .serializers import PostSerializer

# Create your views here.

def main(request):
	return render(request, 'space/main.html', {'title': 'Solar Eclipse'})

def history(request):
	return render(request, 'space/history.html')

def records(request):
	return render(request, 'space/records.html')

def graph(request):
	return render(request, 'space/graph.html')

def comments(request):
	reviews  = {
		'posts' : Post.objects.all()
	}
	return render(request, 'space/comments.html', reviews)


class PostListView(ListView):
	model = Post
	template_name = 'space/comments.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']

class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostView(viewsets.ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
