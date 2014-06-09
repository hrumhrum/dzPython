from django.shortcuts import render_to_response
from mainapp.models import Organization, News, UserProfile

def index(request):
	org = Organization.objects.get(id=1)
	news = News.objects.filter(organization_id=1)
	return render_to_response('mainapp/organization.html', {'desc' : org, 'news' : news})
    