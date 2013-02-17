
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext

def list(request):
    return render_to_response("surveys/list.html", {}, context_instance=RequestContext(request))

def add(request):
    return render_to_response("surveys/add.html", {}, context_instance=RequestContext(request))


def summery(request):
    return render_to_response("surveys/summery.html", {}, context_instance=RequestContext(request))

