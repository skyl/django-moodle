import datetime
from django.http import HttpResponseRedirect  #, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

def home(request):
    context = {}
    return render_to_response('base.html', context, context_instance=RequestContext(request))
