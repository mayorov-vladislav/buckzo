from django.contrib import admin
from .models import Header, Client, Contact, ContactUs


@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title1', 'title2')
    list_editable = ('title1', 'title2')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'order', 'is_visible')
    list_editable = ('name', 'order', 'is_visible')
    search_fields = ('id', 'name', 'order', 'is_visible')
    list_filter = ('id', 'order', 'is_visible')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'is_precessed', 'created_at', 'updated_at')
    list_editable = ('is_precessed', )
    search_fields = ('id', 'name', 'email', 'is_precessed', 'created_at', )
    list_filter = ('id', 'is_precessed')


@admin.register(ContactUs)
class ContactUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email_app', 'phone_app', 'address_app')
    list_editable = ('email_app', 'phone_app', 'address_app')