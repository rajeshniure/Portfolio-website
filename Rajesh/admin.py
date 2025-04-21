from django.contrib import admin
from .models import Profile, Skill, ContactInfo, ContactMessage,Project

# Register your models here.
admin.site.register(Profile)
admin.site.register(Skill)




admin.site.register(ContactInfo)
admin.site.register(ContactMessage)


admin.site.register(Project)

