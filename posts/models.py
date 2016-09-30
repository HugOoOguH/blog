from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# Create your models here.
# 
class Post(models.Model):
	autor = models.ForeignKey(User, related_name="blog_posts")
	titulo = models.CharField(max_length=150)
	contenido = models.TextField()
	fecha = models.DateTimeField(auto_now=True)
	creado = models.DateTimeField(auto_now=True)
	slug = models.SlugField(max_length=200, unique_for_date='creado')
	image = models.ImageField(upload_to="user", blank=True)

	class Meta:
		ordering = ('-creado',)

	def __str__(self):
		return self.titulo

	def get_absolute_url(self):
		return reverse('posts:detail', args=[self.slug])

class Comment(models.Model):
	autor = models.ForeignKey(User, related_name="comentarios")
	post = models.ForeignKey(Post, related_name="comentarios")
	fecha = models.DateTimeField(auto_now=True)
	cuerpo = models.TextField(max_length=140)

	def __str__(self):
		return '{} comento en {}'.format(self.autor, self.post)

	class Meta:
		ordering = ('-fecha',)

