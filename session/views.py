from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from .forms import *
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import HttpResponse

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

def getemail(request):
	if request.method == 'GET':
		if 'user' in request.GET:
			data = User.objects.filter(username=request.GET['user'])
			if data.count() == 1:
				return HttpResponse(data[0].email)
			else:
				return HttpResponse("NotFound")
	return HttpResponse("InvalidFormat")
	
def login(request):
	if request.method == 'POST' and 'username' in request.POST and 'password' in request.POST:
		if request.user.is_authenticated():
			return HttpResponse("loggedIn")
		else:
			return HttpResponse("Invalid Credential")
	return HttpResponse("Invalid Format!")
