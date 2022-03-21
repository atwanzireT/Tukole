from django.contrib import admin
from .models import Address, Member, Ref_Marital_Status

# Register your models here.
admin.site.register(Address)
admin.site.register(Member)
admin.site.register(Ref_Marital_Status)

