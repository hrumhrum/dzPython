from django.shortcuts import render
from mainapp.models import News, Organization, UserProfile
from django.contrib import auth
from django.contrib.auth.models import User
from django.template import RequestContext
from mainapp.gateway import *
from mainapp.domainmodel import *
from mainapp.adapter import *

class UserprofileDmodel:
	id = ''
	user = ''
	organization_id = ''
	privilegies = ''

	def __init__(self, args):
		if hasattr(args, 'id'):
			self.id = args['id']
		if hasattr(args, 'user'):
			self.user = args['user']
		if hasattr(args, 'organization_id'):
			self.organization_id = args['organization_id']
		if hasattr(args, 'privilegies'):
			self.privilegies = args['privilegies']

	def getUser(self, id):
		try:
			userprofileGateway = UserprofileGateway()
			userprofile = userprofileGateway.get(id)
		except UserProfile.DoesNotExist:
			userprofile = None
		return userprofile

class EditLogicDmodel:
	def doEditLogic(self, request):
		user = request.user
		userprofile = UserprofileDmodel({}).getUser(user.id)

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
					editAdapter = AdapterEditOrganization()
					editOrganization = Edit(editAdapter)
					organization = editOrganization.edit(request)
					flag = True
					return render(request, 'mainapp/editorganization.html', {'organizations': organization, 'flag': True})

class OrganizationDmodel:
	id = ''
	name = ''
	addres = ''
	phone = ''
	description = ''

	def getAll(self):
		organizationGateway = OrganizationGateway({})
		return organizationGateway.getAll()

	def get(self, getid):
		organizationGateway = OrganizationGateway({})
		return organizationGateway.get(getid)

	def getId(self, request):
		if request.GET.get('id'):
			getid = request.GET.get('id')
		else:
			getid = 1
		return getid