from django.shortcuts import render
from django.shortcuts import render_to_response
from django.conf import settings
from django.template import RequestContext
from app_teste.models import Blog

# Create your views here.

def index(request):
	params = {}
	params["posts"] = Blog.objects.all()
	return render_to_response('index.html', params, context_instance=RequestContext(request))
