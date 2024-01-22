from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import AboutHeader, Client, Team, MainAboutInfo


@admin.register(AboutHeader)
class AboutHeaderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'job1', 'job2', 'char', 'title2')
    list_editable = ('title', 'job1', 'job2', 'char', 'title2')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'order', 'is_visible', 'client_photo_src_tag')
    list_editable = ('name', 'order', 'is_visible')
    list_filter = ('order', 'is_visible')
    search_fields = ('name', 'order')

    def client_photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50>")

    client_photo_src_tag.short_description = 'Client photo'


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'post', 'order', 'is_visible', 'team_photo_src_tag')
    list_editable = ('name', 'post', 'order', 'is_visible')
    list_filter = ('order', 'is_visible')
    search_fields = ('name', 'order', 'post')

    def team_photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50>")

    team_photo_src_tag.short_description = 'Client photo'


@admin.register(MainAboutInfo)
class MainAboutInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'is_visible', 'main_about_info_photo_src_tag')
    list_editable = ('order', 'is_visible')

    def main_about_info_photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50>")

    main_about_info_photo_src_tag.short_description = 'Main About Info photo'