from django.contrib import admin
from .models import content,userprofile,adminUser
# Register your models here.
admin.site.register(content)
admin.site.register(userprofile)
admin.site.register(adminUser)

