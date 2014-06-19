from mainapp.models import News, Organization, UserProfile
from django.contrib import auth
from django.contrib.auth.models import User
from mainapp.gateway import *

class EditProfile:
	def editProfile(self, request):
		userprofileGateway = UserprofileGateway()
		a = {}
		getid = request.POST['user_id']
		a['first_name'] = request.POST['first_name']
		a['last_name'] = request.POST['last_name']
		a['org'] = request.POST['organization_id']
		a['privilegies'] = request.POST['privilegies']
		userprofile = userprofileGateway.set(getid, a)
		return userprofile

class EditOrganization:
	def editOrganization(self, request):
		organizationGateway = OrganizationGateway({})
		getid = request.POST["orgid"]
		name = request.POST['name']
		addres = request.POST['addres']
		phone = request.POST['phone']
		description = request.POST['description']
		organization = {}
		organization['name'] = name
		organization['addres'] = addres
		organization['phone'] = phone
		organization['description'] = description
		organization = organizationGateway.set(getid, organization)
		return organization

class AdapterEditProfile(EditProfile):
	def edit(self, args):
		return self.editProfile(args)

class AdapterEditOrganization(EditOrganization):
	def edit(self, args):
		return self.editOrganization(args)

class Edit:
	source = ''
	def __init__(self, source):
		self.source = source
	def edit(self, args):
		return self.source.edit(args)