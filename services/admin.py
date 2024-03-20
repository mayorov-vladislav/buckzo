from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Header, ServiceInfo, Client


@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', )
    list_editable = ('title', )


@admin.register(ServiceInfo)
class ServiceInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'order', 'is_visible')
    list_editable = ('title', 'order', 'is_visible')
    search_fields = ('id', 'title', 'order', 'is_visible')
    list_filter = ('id', 'title', 'order', 'is_visible')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link', 'order', 'is_visible', 'client_photo_src_tag')
    list_editable = ('name', 'link', 'order', 'is_visible')
    list_filter = ('id', 'name', 'order', 'is_visible')
    search_fields = ('id', 'name', 'link', 'order')

    def client_photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50>")

    client_photo_src_tag.short_description = 'Client photo'