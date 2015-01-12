from django.shortcuts import render

from principal.models import Jornada, Partido
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

import json,urllib2

def index(request):
    return render_to_response('index.html', context_instance = RequestContext(request))

def jornada(request):
	jors = Jornada.objects.all()
	ret = {}
	lista = []
	for j in jors:
		aux ={}
		aux["id"]=j.id
		aux["nombre"]=j.nombre
		aux["fechadejuego"]=str(j.fechadejuego)
		lista.append(aux)
	ret["result"]=lista
	return HttpResponse( request.GET.get("jsoncallback","") + "(" + json.dumps(ret) + ");" , content_type="application/json")