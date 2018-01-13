from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.template.response import TemplateResponse
from .forms import signupform, create_note_form
from .models import Notes
from django.urls import reverse_lazy
from django.utils import timezone
import datetime
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
			email = form.cleaned_data.get('email')
			phone_no = form.cleaned_data.get('phone_no')
            user = authenticate(username=username, password=raw_password, )

            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


class note_list(ListView):
	model = Notes
	template_name = 'home.html'

def create_note(request):
	form = create_note_form(request.POST)
	if request.method == "POST":
		if form.is_valid():
			instance = form.save(commit=False)
			instance.title = request.POST.get('title')
			instance.description = request.POST.get('description')
			instance.is_pinned = request.POST.get('is_pinned')
			instance.color = request.POST.get('color')
			# instance.user  = request.POST.get('user')
			instance.save()
			# return redirect('home')
	return render(request, 'create_note.html', {'form':form})

class note_details(DetailView):
	model = Notes
	template_name = 'note_detail.html'

class note_update(UpdateView):
	model = Notes
	fields = ['title', 'description', 'is_pinned', 'color']
	template_name = 'note_update.html'

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
