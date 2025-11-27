from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius:50%;" />'.format(object.car_photo.url))
    thumbnail.short_description='car_photo'
    
    list_display = ('id','thumbnail', 'car_title', 'color', 'model','year','body_style','mileage','price','is_featured')
    list_display_links = ('id', 'car_title','thumbnail')
    search_fields = ('id', 'car_title', 'city', 'state', 'model' ,'year','body_style','fuel_type')
    list_editable = ('is_featured',) 
    list_filter = ('model','year','body_style','fuel_type')

admin.site.register(Car,CarAdmin)