from django.contrib import admin
from .models import MCompany, MDepartment, TEmployee

# Register your models here.

admin.site.register(MCompany)
admin.site.register(MDepartment)
admin.site.register(TEmployee)
