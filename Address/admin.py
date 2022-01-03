from django.contrib import admin
from .models import Area,City,Address
# Register your models here.
class TestAdmin(admin.ModelAdmin):
    list_display = ('city','area')

admin.site.register(Area)
admin.site.register(City)
admin.site.register(Address,TestAdmin)