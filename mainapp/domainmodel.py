from mainapp.models import News, Organization, UserProfile
from django.contrib import auth
from django.contrib.auth.models import User
from mainapp.gateway import *

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