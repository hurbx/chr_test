from django.contrib import admin
from .models import Company, Stations


# Register your models here.


class StationsAdmin(admin.ModelAdmin):
    list_display = ('empty_slots', 'address', 'payment', 'last_updated', 'post_code', 'time_stamp', 'company')
    search_fields = ('address', 'payment', 'last_updated', 'post_code', 'time_stamp', 'company')
    list_filter = ('payment',)


admin.site.register(Stations, StationsAdmin)



class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'latitude', 'longitude')
    search_fields = ('name', 'country', 'latitude', 'longitude')
    list_filter = ('name',)


admin.site.register(Company, CompanyAdmin)
