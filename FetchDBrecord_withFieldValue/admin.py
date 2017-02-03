from django.contrib import admin
from Vineet24janapp.models import test, Myproject, Vineettable1, universitydb, collegedb, guestdb, vinymysqlemp, Postxx

@admin.register(Vineettable1)
class FlatPageAdmin(admin.ModelAdmin):
 #fields=(('Name', 'Role'), 'section')
 fieldsets = (
    ("Register New User", {
            'fields': ('Name', 'Role',)
            }),
    ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('section',),
            }),    ) 
 list_display = ('Name','Role','section',)
 readonly_fields = ('Role','section',)
 search_fields = ['Role']


@admin.register(universitydb)
class FlatPageAdmin(admin.ModelAdmin):
 #fields=(('Name', 'Role'), 'section')
 fieldsets = (
    ("Register New User", {
            'fields': ('Name', 'Role',)
            }),
    ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('Address',),
            }),    ) 
 list_display = ('Name','Role','Address',)
 #readonly_fields = ('Role',)
 search_fields = ['Role']
 

# Register your models here.
admin.site.register(test)
admin.site.register(Myproject)
admin.site.register(collegedb)
admin.site.register(guestdb)
admin.site.register(vinymysqlemp)
admin.site.register(Postxx)
#admin.site.register(universitydb)
#admin.site.register(Vineettable1,FlatPageAdmin)