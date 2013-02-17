
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from users.forms import UserForm

from django.template import RequestContext

def login(request):
    form = UserForm()
    return render_to_response("users/login.html", {'form':form}, context_instance=RequestContext(request))

def register(request):
    form = UserForm()
    return render_to_response("users/register.html", {'form':form}, context_instance=RequestContext(request))

