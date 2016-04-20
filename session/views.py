from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from .forms import *
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import HttpResponse

from models import Client
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.


def register(request):
	if request.method == 'POST' :
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(
			username=form.cleaned_data['username'],
			password=form.cleaned_data['password1'],
			email=form.cleaned_data['email']
			)
			return HttpResponseRedirect('/?reg=1')
	else:
		form = RegistrationForm(request.POST)

	return render(request, 'register.html', {'form' : form})



def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')

@login_required
def home(request):
	return render_to_response('home.html',
	{ 'user': request.user }
	)




def index(request):
	return render(request, 'index.html')


def getemail(request):
	if request.method == 'GET':
		if 'user' in request.GET:
			data = User.objects.filter(username=request.GET['user'])
			if data.count() == 1:
				return HttpResponse(data[0].email)
			else:
				return HttpResponse("NotFound")
	return HttpResponse("InvalidFormat")



def getip(request):
	if request.method == 'GET':
		if 'user' in request.GET:
			user = User.objects.filter(username=request.GET['user'])
			if user.count() == 1:
				data = Client.objects.filter(client=user)
				if data.count() == 1:
					return HttpResponse(data[0].ip)
				else:
					return HttpResponse("Not IP")
				
			else:
				return HttpResponse("NotFound")
	return HttpResponse("InvalidFormat")

def setip(request):
	if request.method == 'POST' and 'username' in request.POST and 'password' in request.POST:
		_user = authenticate(username=request.POST['username'], password=request.POST['password'])
        	data = Client.objects.filter(client=user)
       		if data is not None:
				data.ip = request.POST['ip']
				data.save()
				return HttpResponse("Updated")
	return HttpResponse("Error")

def apilogin(request):
	if request.method == 'POST' and 'username' in request.POST and 'password' in request.POST:
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
			return HttpResponse("loggedIn")
		#Invalid Credential	
	return HttpResponse("Invalid Format!")

def apiAllIp(request):
	clients = Client.objects.all()
	mymap = []
	for client in clients:
		mymap.append({'ip':client.ip, 'name':client.client.username})
	data = {'data':mymap}
	return HttpResponse(JsonResponse(data).content)
