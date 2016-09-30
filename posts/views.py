from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.utils.text import slugify
from .models import Post
from .forms import PostForm, CommentForm
# Create your views here.
 
class PostList(View):
	def get(self,request):
		template = "posts/list_view.html"
		user = User.objects.get(username="hugo")
		posts = user.blog_posts.all()
		context = {
			'posts':posts
		}
		return render(request, template, context)

class DetailView(View):
	def get(self,request,slug):
		template_name = "posts/detail.html"
		form = CommentForm()
		post = Post.objects.get(slug=slug)
		comentarios = post.comentarios.all()
		context = {
			'post':post,		
			'comentarios':comentarios,
			'form':form,
		}
		return render(request,template_name,context)

	def post(self,request,slug):
		form  = CommentForm(request.POST)
		post = Post.objects.get(slug=slug)
		form = form.save(commit=False)
		form.autor = request.user
		form.post = post
		form.save()
		return redirect('posts:detail',slug=slug)		


class NuevoPost(View):
	def get(self,request):
		form = PostForm()
		template_name = "posts/new.html"
		context = {
		'form':form
		}
		return render(request, template_name, context)

	def post(self,request):
		form = PostForm(request.POST)
		post = form.save(commit=False)
		post.slug = slugify(post.titulo)
		post.autor = request.user
		post.save()

		return redirect('posts:post_list')

