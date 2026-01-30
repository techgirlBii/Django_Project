from django.contrib import admin
from . models import Item, Content

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'phone')

class ContentAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'phone')

admin.site.register(Item, ItemAdmin)
admin.site.register(Content, ContentAdmin)