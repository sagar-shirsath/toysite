
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from users.forms import UserForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import logout


from django.template import RequestContext

def login(request):
    form = UserForm()
    return render_to_response("users/login.html", {'form':form}, context_instance=RequestContext(request))

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            request.flash['message'] = "You can login now..."
            return HttpResponseRedirect("/user/login")
    else:
        form = UserCreationForm()

    return render_to_response("users/register.html", {'form':form}, context_instance=RequestContext(request))

def logout_me(request):
    logout(request)
    return HttpResponseRedirect("/user/login")




