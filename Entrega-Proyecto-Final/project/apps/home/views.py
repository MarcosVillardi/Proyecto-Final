from django.shortcuts import render
from . import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.admin.views.decorators import staff_member_required

def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def confirm(request):
    return render(request, 'home/confirm.html')
@staff_member_required
def register_request(request):
      if request.method == 'POST':
            form = forms.CustomUserCreationForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"home/index.html" ,)
      else:
           form = forms.CustomUserCreationForm()      
      return render(request,"home/register.html",{"form":form})
