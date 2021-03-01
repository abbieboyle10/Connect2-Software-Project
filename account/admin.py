from django.contrib import admin
from .models import User, Employee, Employer, Job, Skill, Tag, Experience
# Register your models here.
admin.site.register(User)
admin.site.register(Employee)
admin.site.register(Employer)
admin.site.register(Job)
admin.site.register(Skill)
admin.site.register(Tag)
admin.site.register(Experience)
