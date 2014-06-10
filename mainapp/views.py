# -*- coding: utf-8 -*-

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

def organization(request):
	user = request.user
	if request.GET.get('id'):
		getid = request.GET.get('id')
	else:
		getid = 1
	try:
		userprofile = UserProfile.objects.get(user_id=user.id)
	except UserProfile.DoesNotExist:
		userprofile = None
	organizations = Organization.objects.get(id = getid)
	news = News.objects.filter(organization_id = getid)
	return render(request, 'mainapp/organization.html', {'desc': organizations, 'userprofile': userprofile, 'news' : news})

def search(request):
	query = request.POST["search"]
	user = request.user
	try:
		userprofile = UserProfile.objects.get(user_id=user.id)
	except UserProfile.DoesNotExist:
		userprofile = None

	organizations = Organization.objects.filter(name__contains=query)
	return render(request, 'mainapp/index.html', {'poll': organizations, 'userprofile': userprofile})

def users_list(request):
	user = request.user
	try:
		userprofile = UserProfile.objects.get(user_id=user.id)
	except UserProfile.DoesNotExist:
		userprofile = None
	users = UserProfile.objects.filter(privilegies__contains='Менеджер')
	org = Organization.objects.all()
	return render(request, 'mainapp/users_list.html', {'users' : users, 'org' : org})

def edit(request):
	user = request.user
	try:
		userprofile = UserProfile.objects.get(user_id=user.id)
	except UserProfile.DoesNotExist:
		userprofile = None

	if userprofile == None:
		return render(request, 'mainapp/403.html')
	else:		
		if userprofile.privilegies != 'admin':
			return render(request, 'mainapp/403.html')
		else:
			if request.GET.get('id'):
				getid = request.GET.get('id')
				organization = Organization.objects.get(id = getid)
				return render(request, 'mainapp/editorganization.html', {'organizations': organization})
			if request.POST:
				getid = request.POST["orgid"]
				name = request.POST['name']
				addres = request.POST['addres']
				phone = request.POST['phone']
				description = request.POST['description']
				organization = Organization.objects.get(id = getid)
				organization.name = name
				organization.addres = addres
				organization.phone = phone
				organization.description = description
				organization.save()
				flag = True
				return render(request, 'mainapp/editorganization.html', {'organizations': organization, 'flag': True})
