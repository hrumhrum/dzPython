from django.contrib import admin
from mainapp.models import Organization, News, UserProfile
from django.contrib.auth.models import User


admin.site.register(Organization)
admin.site.register(News)
admin.site.register(UserProfile)

# Register your models here.
