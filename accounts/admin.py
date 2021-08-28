from django.contrib import admin
from accounts.models import NewUser, Project, Proposal, Contract

# Register your models here.

admin.site.register(NewUser)
admin.site.register(Project)
admin.site.register(Proposal)
admin.site.register(Contract)
