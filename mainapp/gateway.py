from mainapp.models import News, Organization, UserProfile
from django.contrib import auth
from django.contrib.auth.models import User

class OrganizationGateway:
    id = ''
    name = ''
    addres = ''
    phone = ''
    description = ''

    def __init__(self, args):
        if hasattr(args, 'name'):
            self.name = args['name']
        if hasattr(args, 'addres'):
            self.addres = args['addres']
        if hasattr(args, 'phone'):
            self.phone = args['phone']
        if hasattr(args, 'description'):
            self.description = args['description']

    def get(self, id):
        org = Organization.objects.get(id = id)
        self.id = org.id
        self.name = org.name
        self.addres = org.addres
        self.phone = org.phone
        self.description = org.description
        return self

    def getAll(self):
        return Organization.objects.all()

    def set(self, id, args):
        organization = Organization.objects.get(id = id)
        organization.name = args['name']
        organization.addres = args['addres']
        organization.phone = args['phone']
        organization.description = args['description']
        organization.save()
        return organization

class UserprofileGateway:
	id = ''
	user = ''
	organization_id = ''
	privilegies = ''

	def get(self, id):
		userprofile = UserProfile.objects.get(id = id)
		self.id = userprofile.id
		self.user = User.objects.get(id = userprofile.user_id)
		self.organization_id = Organization.objects.get(id = userprofile.organization_id_id)
		self.privilegies = userprofile.privilegies
		return self

	def set(self, id, args):
		userprofile = UserProfile.objects.get(id = id)
		user = User.objects.get(id = userprofile.user_id)
		organization = Organization.objects.get(id = userprofile.organization_id_id)
		user.first_name = args['first_name']
		user.last_name = args['last_name']
		user.save()
		organization.name = args['org']
		organization.save()
		userprofile.privilegies = args['privilegies']
		userprofile.save()
		return userprofile

