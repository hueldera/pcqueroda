from django.contrib import admin
from .models import Software, Computer, LeadList

admin.site.register(Software)
admin.site.register(LeadList)
admin.site.register(Computer)