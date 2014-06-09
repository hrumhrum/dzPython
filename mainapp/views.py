from django.shortcuts import render
from mainapp.models import News, Organization, UserProfile
from django.contrib import auth
from django.contrib.auth.models import User
from django.template import RequestContext

def index(request):
	user = request.user
	try:
		userprofile = UserProfile.objects.get(user_id=user.id)
	except UserProfile.DoesNotExist:
		userprofile = None

	organizations = Organization.objects.all()
	return render(request, 'mainapp/index.html', {'poll': organizations, 'userprofile': userprofile})
    