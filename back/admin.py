from django.contrib import admin
from django.contrib.auth.models import Group,User
from django.utils.html import mark_safe
from .models import *
from import_export.admin import ExportActionMixin
# Register your models here.

admin.site.site_header = 'Pinnamaya Administration'
admin.site.unregister(Group)
admin.site.unregister(User)
# admin.site.register(Product)
# admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Image)
admin.site.register(Event)

class EmailAdmin(ExportActionMixin, admin.ModelAdmin):
    readonly_fields = ['email']



admin.site.register(Email,EmailAdmin)


class ColorAdmin(admin.ModelAdmin):
    list_display = ['colorsm']
    def colorsm(self, obj):
        return mark_safe('<div style="display: flex;align-items: center;"><div style="width: 30px;height: 30px;background-color: %s;border-radius: 15px;"></div><p>%s (%s)</p></div>' % (obj.color,obj.colorname,obj.of.model) )

admin.site.register(Color, ColorAdmin)
class ColorInline(admin.TabularInline):
    model = Color
    def get_extra(self, request, obj=None, **kwargs):
        return 0

class SizeInline(admin.TabularInline):
    model = Size
    def get_extra(self, request, obj=None, **kwargs):
        return 0

class ProductAdmin(ExportActionMixin, admin.ModelAdmin):
    # form = ProductForm
    # fields = ['__all__']
    list_filter = ['model']
    list_display = ('model', 'description')
    inlines = [ColorInline,SizeInline]

admin.site.register(Product,ProductAdmin)