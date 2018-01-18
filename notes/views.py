from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.template.response import TemplateResponse
from .forms import SignUpForm, create_note_form, registrationForm, loginForm, update_note_form
from .models import Notes
from django.urls import reverse_lazy
from django.utils import timezone
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import json
from django.db import IntegrityError

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('home')
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form': form})

def register(request):
	if request.method == 'POST':
		response_data = {}
		form = registrationForm(request.POST)
		if form.is_valid():
			# user was retrieved
			first_name = form.cleaned_data.get('first_name')
			last_name = form.cleaned_data.get('last_name')
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password')
			email = form.cleaned_data.get('email')
			if first_name and username and raw_password:
				try:
					User.objects.get(username=username)
					response_data['status'] = False
					response_data['message'] = 'User already registered'
				except User.DoesNotExist:
					try:
						user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=raw_password, email=email)
						response_data['status'] = True
						response_data['message'] = 'Successfull registered user'
					except IntegrityError as e:
						response_data['status'] = False
						response_data['message'] =  e.message
			else:
				response_data['status'] = False
				response_data['message'] = 'Fill all the fields'
		else:
			response_data['status'] = False
			response_data['message'] = 'Failed to register'
		return HttpResponse(json.dumps(response_data), content_type='application/json')
	else:
		form = registrationForm()
		return render(request, 'register.html', {'form':form})

class Login(TemplateView):
	def get(self, request, *args, **kwargs):
		response_data = {}
		form = loginForm()
		if request.user.is_authenticated:
			return redirect(reverse('home'))
		# else:
		# self.template_name = 'registration/login.html'
		# return render(request,'login.html')
		return render(request, 'login.html', {'form':form})

	def post(self, request, *args, **kwargs):
		# username = request.POST.get('username', '')
		response_data = {}
		form = loginForm(request.POST)
		username = request.POST.get('username')
		password = request.POST.get('password')
		if username and password:
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				response_data['status'] = True
				response_data['message'] = "Logged In Successfully"
			else:
				response_data['status'] = False
				response_data['message'] =  "Username and password does not match.."
		else:
			response_data['status'] = False
			response_data['message'] = 'Fill all the fields'

		return HttpResponse(json.dumps(response_data), content_type='application/json')

def login_user(request):
	if request.method == 'POST':
		response_data = {}
		form = loginForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		if username and password:
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				response_data['status'] = True
				response_data['message'] = "Logged In Successfully"
			else:
				response_data['status'] = False
				response_data['message'] =  "Username and password does not match.."
		else:
			response_data['status'] = False
			response_data['message'] = 'Fill all the fields'
		return HttpResponse(json.dumps(response_data), content_type='application/json')
	form = loginForm()
	return render(request, 'login.html', {'form':form})

class note_list(ListView):
	''' This is a class based view of django which uses ListView.
	    it returns object_list of objects in database.'''
	model = Notes
	template_name = 'home.html'

def create_note(request):
	try:
		form = create_note_form(request.POST)
		if request.method == "POST":
			response_data = {}
			if form.is_valid():
				instance = form.save(commit=False)
				instance.title = request.POST.get('title')
				instance.description = request.POST.get('description')
				instance.is_pinned = request.POST.get('is_pinned')
				instance.color = request.POST.get('color')
				# instance.user  = request.POST.get('user')
				instance.save()
				response_data['status'] = True
				response_data['message'] = 'Successfully Filled data'
				return HttpResponse(json.dumps(response_data), content_type='application/json')
			# return redirect('home')
	except Exception as e:
		response_data['status'] = False
		response_data['message'] = 'something went wrong'
	return render(request, 'home.html', {'form':form})

class note_details(DetailView):
	model = Notes
	template_name = 'note_detail.html'

# class note_edit(TemplateView):
def note_edit(request, pk):
	note = Notes.objects.get(id=pk)
	print("note = ",note)
	# form = update_note_form(request.POST)
	# for name, value in request.POST.items()
	return render(request, 'note_update.html', {'note':note})

class note_update(UpdateView):
	def post(self, request, *args, **kwargs):
		response_data = {}
		response_data['status'] = False
		if kwargs.get('pk', None):
			try:
				pk = kwargs.get('pk', None)
				obj = Notes.objects.get(pk=pk)
				obj.title = request.POST.get('title')
				obj.description = request.POST.get('description')
				obj.is_pinned = request.POST.get('is_pinned')
				obj.color = request.POST.get('color')
				obj.save()
				response_data['status'] = True
				response_data['message'] = "Updated Successfully"
			except Exception(DoesNotExist):
				response_data['message'] = "Note doesnt exists"
			except Exception as e:
				response_data['message'] = 'something went wrong'
		else:
			response_data['message'] = "Missing note identifier (id)"
		return HttpResponse(json.dumps(response_data), content_type='application/json')

	def get(self, request, *args, **kwargs):
		print("in get call")
		response_data = {}
		for name, value in request.POST.items():
			print("name = ",name)   #dict.items()
			Notes(**dict( [ (name, value) ] )).save()
		response_data['status'] = False
		response_data['message'] = "Note not found.."
		return HttpResponse(json.dumps(response_data), content_type='application/json')

class note_delete(DeleteView):
	model = Notes
	template_name = 'note_delete.html'
	success_url = reverse_lazy('home')

class note_unpinned(ListView):
	model = Notes
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context

class note_pinned(UpdateView):
	model = Notes
	fields = ['is_pinned']
	template_name = 'note_pinned.html'

class note_archived(UpdateView):
	model = Notes
	fields = ['is_archived']
	template_name = 'note_archived.html'

class note_lable(UpdateView):
	model = Notes
	fields = ['label']
	template_name = 'note_lable.html'

class note_reminder(UpdateView):
	now = datetime.datetime.now()
	model = Notes
	fields = ['remainder']
	template_name = 'note_reminder.html'

class note_colaborator(UpdateView):
	model=Notes
	fields=['collaborate']
	template_name = 'note_collaborate.html'

# def reminder_fun():
# 	now = datetime.datetime.now()
# 	print("now = ",now)
# 	if now == reminder
