
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

@login_required
def list(request):
    return render_to_response("surveys/list.html", {}, context_instance=RequestContext(request))
@login_required
def add(request):
    return render_to_response("surveys/add.html", {}, context_instance=RequestContext(request))

@login_required
def summery(request):
    return render_to_response("surveys/summery.html", {}, context_instance=RequestContext(request))

