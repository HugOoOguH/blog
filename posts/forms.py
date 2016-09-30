from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['titulo', 'contenido']

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['cuerpo',]
		label = {
			'cuerpo':'Escribe un comentario'
		}