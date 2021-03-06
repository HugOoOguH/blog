from django.shortcuts import render, redirect
from django.views.generic import View 
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile
# Create your viewshere.

class Registration(View):
	def get(self,request):
		template_name = "registration/registration.html"
		form = UserRegistrationForm()
		context = {
		'form':form,
		}
		return render(request,template_name,context)

	def post(self,request):
		template_name = "registration/registration.html"
		new_user_form = UserRegistrationForm(request.POST)
		if new_user_form.is_valid():
			new_user = new_user_form.save(commit=False)
			new_user.set_password(new_user_form.cleaned_data['password'])
			new_user.save()
			perfil = Profile()
			perfil.user = new_user
			perfil.save()
			return redirect('home')

class Dashboard(View):
	@method_decorator(login_required)
	def get(self,request):
		template_name = "registration/profile.html"
		userform = UserEditForm(instance=request.user)
		profileform = ProfileEditForm(instance=request.user.profile)
		context = {
		'userform':userform,
		'profileform':profileform,
		}
		return render(request,template_name, context)

	def post(self, request):
		template_name = "registration/profile.html"
		userform = UserEditForm(instance=request.user, data=request.POST)
		profileform = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
		if userform.is_valid() and profileform.is_valid():
			userform.save()
			profileform.save()
			return redirect('home')
		else:
			context = {
			'userform':userform,
			'profileform':profileform,
			}
			return render(request, template_name, context)

class NewClass(View):
	pass

