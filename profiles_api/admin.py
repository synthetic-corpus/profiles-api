from django.contrib import admin

from profiles_api import models

# Register your models here.
# Registering them here makes them accessible via an admin CLI account.

admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)