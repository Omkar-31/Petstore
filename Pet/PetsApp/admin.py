from django.contrib import admin

# Register your models here.
from .models import *

class PetAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name","breed")}


admin.site.register(Pet,PetAdmin)
admin.site.register(Cart)
admin.site.register(Customers)
admin.site.register(BillingDetail)