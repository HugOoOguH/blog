from __future__ import unicode_literals
from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
	BOOL_CHOICES = ((True, 'Man'), (False, 'Woman'))
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	age = models.IntegerField(blank=True, null=True)
	sex = models.BooleanField(choices=BOOL_CHOICES, default=True)
	photo = models.ImageField(upload_to="users/%Y/%m/%d", blank=True)

	class Meta:
		ordering = ('user',)

	def __str__(self):
		return 'Perfil del usuario {}'.format(self.user.username)