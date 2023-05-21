from django.contrib import admin


# Register your models here.
from .models import Add_vehicle
from .models import Category

class AddAdmin(admin.ModelAdmin):
        list_display = ('id','vehicle_no','vehicle_type','parking_area_no','parking_charge','arrival_time','status')
        list_display_links = ('id','parking_area_no',)
        list_filter = ('parking_charge',)
        search_fields = ('vehicle_no', 'parking_charge')
admin.site.register(Add_vehicle,AddAdmin)


class CatAdmin(admin.ModelAdmin):
        list_display = ('id','parking_area_no', 'vehicle_limit', 'vehicle_type', 'parking_charge', 'status', 'arrival_time')
        list_display_links = ('id','parking_area_no',)
        list_filter = ('parking_charge',)
        search_fields = ('vehicle_no', 'parking_charge',)

admin.site.register(Category,CatAdmin)








