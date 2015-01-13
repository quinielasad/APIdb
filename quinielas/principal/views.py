from django.shortcuts import render

from principal.models import Jornada, Partido
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

#authentication
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password

import json,urllib2

#generict views
#def jornada(request):
#	var = Objeto.objects.all()
#	ret = {}	
#	return HttpResponse( request.GET.get("jsoncallback","") + "(" + json.dumps(ret) + ");" , content_type="application/json")

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

def loginUser(request):
	ret={}
	data_in = request.GET.get("data", "no_data")
	data = []
	if data_in != "no_data":
		try:
			object_in = json.loads(data_in)

			if object_in["username"]:	
				data = User.objects.filter( username=object_in["username"])
				if check_password(object_in["password"], data[0].password ):
					ret["status"]="OK"
					ret['message']="Permitir login."
					ret["datos"] = data[0].username
				else:
					ret["status"]="ERROR"
					ret['message']="El usuario o la password no es valida."
			else:
				ret["status"]="ERROR"
				ret['message']="El usuario no existe."
		except Exception: 
			ret["status"]="ERROR"
			ret['message']="La cadena json esta mal formada."
	else:
		ret["status"]="ERROR"
		ret['message']="El parametro data es obligatorio."	

	return HttpResponse( request.GET.get("jsoncallback","") + "(" + json.dumps(ret) + ");" , content_type="application/json")
