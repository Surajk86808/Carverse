from django.contrib import admin
from .models import Team
from django.utils.html import format_html

class TeamAdmin(admin.ModelAdmin):
    def Thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius:50%;" />'.format(object.photo.url))
    
    Thumbnail.short_description='Photo'
    
    list_display = ('id','Thumbnail','first_name', 'last_name', 'designation', 'created_at', 'updated_at')
    list_display_links = ('id', 'first_name',)
    search_fields = ('first_name', 'last_name', 'designation')
    list_filter = ('designation',)
    
    
# Register your models here.
admin.site.register(Team, TeamAdmin)