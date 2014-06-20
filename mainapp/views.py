# -*- coding: utf-8 -*-

from django.shortcuts import render
from mainapp.models import News, Organization, UserProfile
from django.contrib import auth
from django.contrib.auth.models import User
from django.template import RequestContext
from mainapp.gateway import *
from mainapp.domainmodel import *
from mainapp.adapter import *


def index(request):
	user = request.user
	userprofile = UserprofileDmodel({}).getUser(user.id) #domainmodel
	#organizationGateway = OrganizationGateway({}) #gateway
	organizations = OrganizationDmodel().getAll()
	return render(request, 'mainapp/index.html', {'poll': organizations, 'userprofile': userprofile})

def organization(request):
	user = request.user
	getid = OrganizationDmodel().getId(request)
	userprofile = UserprofileDmodel({}).getUser(user.id)
	organizations = OrganizationDmodel().get(getid)

	news = News.objects.filter(organization_id = getid) #!!
	return render(request, 'mainapp/organization.html', {'desc': organizations, 'userprofile': userprofile, 'news' : news})

def search(request):
	query = request.POST["search"]
	user = request.user
	userprofile = UserprofileDmodel({}).getUser(user.id)	
	organizations = Organization.objects.filter(name__contains=query) #!!
	return render(request, 'mainapp/index.html', {'poll': organizations, 'userprofile': userprofile})

def users_list(request):
	user = request.user
	userprofile = UserprofileDmodel({}).getUser(user.id)
	users = UserProfile.objects.filter(privilegies__contains='manager')
	org = OrganizationDmodel().getAll()
	return render(request, 'mainapp/users_list.html', {'users' : users, 'org' : org})

def edit(request):
	return EditLogicDmodel().doEditLogic(request)

def edituser(request):
	user = request.user
	userprofile = UserprofileDmodel({}).getUser(user.id)
	userprofileGateway = UserprofileGateway()
	if userprofile == None:
		return render(request, 'mainapp/403.html')
	else:		
		if userprofile.privilegies != 'admin':
			return render(request, 'mainapp/403.html')
		else:
			if request.GET.get('id'):
				getid = request.GET.get('id')
				userprofile = UserprofileDmodel({}).getUser(getid)
				return render(request, 'mainapp/edituser.html', {'users' : userprofile})
			if request.POST:
				editAdapter = AdapterEditProfile()
				editUser = Edit(editAdapter)
				userprofile = editUser.edit(request)

				flag = True
				return render(request, 'mainapp/edituser.html', {'users' : userprofile, 'flag': True})


