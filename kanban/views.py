from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, resolve_url
from django.views.generic import DetailView, UpdateView

from .forms import UserForm

from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "kanban/index.html") 

def home(request):
    return render(request, "kanban/home.html")

def signup(request):
  if request.method =='POST':
      form = UserCreationForm(request.POST)
      if form.is_valid():
        user_instance = form.save()
        login(request, user_instance)
        return redirect("kanban:home")
  else:
    form = UserCreationForm()

  context = {
    "form": form
  }
  return render(request, 'kanban/signup.html', context)

@login_required
def home(request):
    return render(request, "kanban/home.html")

class UserDetailView(DetailView):
  model = User
  template_name ="kanban/users/detail.html"

class UserUpdateView(UpdateView):
  model = User
  template_name = "kanban/users/update.html"
  