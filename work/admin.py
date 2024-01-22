from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Header, Work, WorkCategory

admin.site.register(WorkCategory)


@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title1', 'title2')
    list_editable = ('title1', 'title2')


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'order', 'work_category', 'is_visible', 'main_work_photo_src_tag')
    list_editable = ('title', 'work_category', 'order', 'is_visible')
    search_fields = ('id', 'title', 'work_category', 'order')
    list_filter = ('id', 'work_category', 'order', 'is_visible')

    def main_work_photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50>")

    main_work_photo_src_tag.short_description = 'Work photo'