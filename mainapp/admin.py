from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Header, MainInfo, Work, WorkCategory, Footer


@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_editable = ('title', )


@admin.register(MainInfo)
class MainInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'order', 'is_visible')
    list_editable = ('title', 'order', 'is_visible')
    search_fields = ('title', 'order')
    list_filter = ('order', 'is_visible')


@admin.register(WorkCategory)
class WorkCategoryAdmin(admin.ModelAdmin):
   list_display = ("id", 'name', 'is_visible', 'order')
   list_editable = ('name', 'order', 'is_visible')
   search_fields = ('id', 'name', 'order')
   list_filter = ('id', 'order', 'is_visible')


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("id", 'name', 'order', 'work_category', 'is_visible', 'work_photo_src_tag')
    list_editable = ('name', 'order', 'work_category', 'is_visible', )
    search_fields = ('name', 'order', 'work_category', 'is_visible')

    def work_photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50>")

    work_photo_src_tag.short_description = 'Work photo'


admin.site.register(Footer)
